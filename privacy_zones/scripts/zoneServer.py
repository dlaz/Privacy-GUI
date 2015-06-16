#!/usr/bin/env python

from privacy_zones.map_geometry import MapGeometry, Zones
from privacy_zones.msg import Transition, ZoneControl
from privacy_zones.srv import DevicesInZone, DevicesInZoneRequest, DevicesInZoneResponse
from privacy_zones.srv import LocalizeInZone, LocalizeInZoneRequest, LocalizeInZoneResponse
from privacy_zones.srv import GetZoneLocations, GetZoneLocationsRequest, GetZoneLocationsResponse
from std_srvs.srv import Empty as EmptySrv, EmptyResponse
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, PolygonStamped
from peac_bridge.srv import GetDeviceInfo, GetDeviceInfoRequest, ListLocations, ListDevices
from nav_msgs.msg import Odometry
from nav_msgs.srv import GlobalLocalizationPolygon, GlobalLocalizationPolygonRequest
from shapely.geometry import Point
import sys
import yaml
import rospy
import tf

from threading import RLock

class ZoneServer(object):
    def __init__(self, zone_file_path, map_info_path, zone_controls_path):
        with open(zone_file_path, 'r') as zone_file:
            zones = yaml.load(zone_file)['Zone List']

        with open(zone_controls_path, 'r') as zone_controls_file:
            self.zone_controls = yaml.load(zone_controls_file)

        self.geom = MapGeometry(map_info_path)
        self.zones = Zones(zones, self.geom)
        self.current_zones = []
        self.previous_zones = []
        self.last_transition_time = rospy.Time(0)
        
        self.tfl = tf.TransformListener()

        self.list_devices_lock = RLock()

        rospy.Subscriber('pose', PoseStamped, self.pose_cb)
        rospy.Subscriber('odom', Odometry, self.odom_cb)
        rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, self.pose_with_cov_cb)
        self.get_device_info = rospy.ServiceProxy('peac/get_device_info', GetDeviceInfo)
        self.list_locations = rospy.ServiceProxy('peac/list_locations', ListLocations)
        self.list_devices = rospy.ServiceProxy('peac/list_devices', ListDevices)
        self.polygon_localization = rospy.ServiceProxy('polygon_localization', GlobalLocalizationPolygon)
        self.global_localization = rospy.ServiceProxy('global_localization', EmptySrv)
        self.transition_pub = rospy.Publisher('transition', Transition, latch=True)
        rospy.Service('get_devices_in_zone', DevicesInZone, self.handle_list_devices)
        rospy.Service('get_zone_locations', GetZoneLocations, self.get_zone_locations)
        rospy.Service('localize_in_zone', LocalizeInZone, self.localize_in_zone)

    def handle_list_devices(self, req):
        with self.list_devices_lock:
            control_cache = {}
            zcs = []
            for control in self.zone_controls.get(req.zone, []):
                if control['controlId'] not in control_cache:
                    for cc in self.get_device_info(control['deviceId']).controls:
                        control_cache[cc.controlId] = cc

                zcs.append(ZoneControl(
                    zone=req.zone,
                    controlId=control['controlId'],
                    deviceId=control['deviceId'],
                    name=control['control'],
                    numVal=control_cache[control['controlId']].numVal)
                )
            return DevicesInZoneResponse(zcs)

    def pose_cb(self, msg):
        msg.header.stamp = rospy.Time(0)
        msg_trans = self.tfl.transformPose('map', msg)
        pt = Point(msg_trans.pose.position.x, msg_trans.pose.position.y)
        within_zones = self.zones.in_which(pt)
        if within_zones:
            self.previous_zones = self.current_zones
            self.current_zones = within_zones
            self.check_transition()

    def pose_with_cov_cb(self, msg):
        pose = PoseStamped()
        pose.header = msg.header
        pose.pose = msg.pose.pose
        self.pose_cb(pose)

    def odom_cb(self, msg):
        pose = PoseStamped()
        pose.header = msg.header
        pose.pose = msg.pose.pose
        self.pose_cb(pose)

    def get_peac_locations(self, zone):
        name = zone
        if type(zone) != str:
            name = zone.name
        devices = self.handle_list_devices(DevicesInZoneRequest(name))
        device_ids = set([c.deviceId for c in devices.controls])
        locations = self.list_locations()
        matched_locations = []
        for location in locations.locations:
            loc_devices = self.list_devices(location.locationId)
            loc_device_ids = set([c.deviceId for c in loc_devices.devices])

            # if any of our devices are also in this location, add it
            if device_ids.intersection(loc_device_ids):
                matched_locations.append(location)
        return matched_locations

    def get_zone_locations(self, req):
        resp = GetZoneLocationsResponse()
        for zone, zone_info in self.zones.iteritems():
            locs = self.get_peac_locations(zone)
            for loc in locs:
                resp.zones.append(zone_info.to_msg())
                resp.locations.append(loc)
        return resp


    def localize_in_zone(self, zone_req):
        print zone_req.zone
        if zone_req.zone == 'NONE':
            # If user isn't in a predefined zone, what should we do?
            # For now, try global localization
            self.global_localization()
        else:
            zone = self.zones[zone_req.zone]
            zone_poly = zone.to_msg().zone
            poly_stamped = PolygonStamped()
            req = GlobalLocalizationPolygonRequest(poly=poly_stamped)
            poly_stamped.polygon = zone_poly
            poly_stamped.header.frame_id = zone.gen.frame_id
            self.polygon_localization(req)
        return LocalizeInZoneResponse()

    def check_transition(self):
        # if self.previous_zones and self.current_zones:
        if self.current_zones: # this will trigger a transition on startup for the current zone
            entered_zones = set(self.current_zones) - set(self.previous_zones)
            exited_zones = set(self.previous_zones) - set(self.current_zones)
            for zone in exited_zones:
                transition_msg = Transition(
                    action=Transition.EXIT,
                    zone=zone.to_msg(),
                    peac_locations=self.get_peac_locations(zone)
                )
                self.transition_pub.publish(transition_msg)
            for zone in entered_zones:
                transition_msg = Transition(
                    action=Transition.ENTER,
                    zone=zone.to_msg(),
                    peac_locations=self.get_peac_locations(zone)
                )
                self.transition_pub.publish(transition_msg)

if __name__ == '__main__':
    rospy.init_node('zone_server')
    server = ZoneServer(sys.argv[1], sys.argv[2], sys.argv[3])
    rospy.spin()
