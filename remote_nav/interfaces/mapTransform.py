# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapTransform.ui'
#
# Created: Thu Aug  7 11:56:57 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(838, 638)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Window)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter = QtGui.QSplitter(Window)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.source = customView(self.splitter)
        self.source.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.source.setMouseTracking(False)
        self.source.setObjectName(_fromUtf8("source"))
        self.destination = customView(self.splitter)
        self.destination.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.destination.setObjectName(_fromUtf8("destination"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.export_btn = QtGui.QPushButton(self.layoutWidget)
        self.export_btn.setObjectName(_fromUtf8("export_btn"))
        self.verticalLayout.addWidget(self.export_btn)
        self.transform_btn = QtGui.QPushButton(self.layoutWidget)
        self.transform_btn.setObjectName(_fromUtf8("transform_btn"))
        self.verticalLayout.addWidget(self.transform_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.tools = QtGui.QTabWidget(self.layoutWidget)
        self.tools.setObjectName(_fromUtf8("tools"))
        self.affine_tool = QtGui.QWidget()
        self.affine_tool.setObjectName(_fromUtf8("affine_tool"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.affine_tool)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loadPoint_btn = QtGui.QPushButton(self.affine_tool)
        self.loadPoint_btn.setObjectName(_fromUtf8("loadPoint_btn"))
        self.horizontalLayout_2.addWidget(self.loadPoint_btn)
        self.exportPoint_btn = QtGui.QPushButton(self.affine_tool)
        self.exportPoint_btn.setObjectName(_fromUtf8("exportPoint_btn"))
        self.horizontalLayout_2.addWidget(self.exportPoint_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.affine_tool)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.label_6 = QtGui.QLabel(self.affine_tool)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.clearUnmatched_btn = QtGui.QPushButton(self.affine_tool)
        self.clearUnmatched_btn.setObjectName(_fromUtf8("clearUnmatched_btn"))
        self.verticalLayout_2.addWidget(self.clearUnmatched_btn)
        self.clearAll_btn = QtGui.QPushButton(self.affine_tool)
        self.clearAll_btn.setObjectName(_fromUtf8("clearAll_btn"))
        self.verticalLayout_2.addWidget(self.clearAll_btn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.affine_tool)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtGui.QLabel(self.affine_tool)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.affine_tool)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.affine_tool)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tools.addTab(self.affine_tool, _fromUtf8(""))
        self.zone_tool = QtGui.QWidget()
        self.zone_tool.setObjectName(_fromUtf8("zone_tool"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.zone_tool)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.importZone_btn = QtGui.QPushButton(self.zone_tool)
        self.importZone_btn.setObjectName(_fromUtf8("importZone_btn"))
        self.verticalLayout_3.addWidget(self.importZone_btn)
        self.label_2 = QtGui.QLabel(self.zone_tool)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.zoneData = QtGui.QTextEdit(self.zone_tool)
        self.zoneData.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.zoneData.setReadOnly(True)
        self.zoneData.setAcceptRichText(False)
        self.zoneData.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.zoneData.setObjectName(_fromUtf8("zoneData"))
        self.verticalLayout_3.addWidget(self.zoneData)
        self.exportZone_btn = QtGui.QPushButton(self.zone_tool)
        self.exportZone_btn.setObjectName(_fromUtf8("exportZone_btn"))
        self.verticalLayout_3.addWidget(self.exportZone_btn)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.tools.addTab(self.zone_tool, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tools)
        self.toggleRobot = QtGui.QCheckBox(self.layoutWidget)
        self.toggleRobot.setObjectName(_fromUtf8("toggleRobot"))
        self.verticalLayout.addWidget(self.toggleRobot)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(Window)
        self.tools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)
        Window.setTabOrder(self.source, self.destination)
        Window.setTabOrder(self.destination, self.export_btn)
        Window.setTabOrder(self.export_btn, self.transform_btn)
        Window.setTabOrder(self.transform_btn, self.toggleRobot)

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.export_btn.setText(QtGui.QApplication.translate("Window", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.transform_btn.setText(QtGui.QApplication.translate("Window", "Preview Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPoint_btn.setToolTip(QtGui.QApplication.translate("Window", "Loads a file of saved points on a map", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPoint_btn.setText(QtGui.QApplication.translate("Window", "Load Points", None, QtGui.QApplication.UnicodeUTF8))
        self.exportPoint_btn.setToolTip(QtGui.QApplication.translate("Window", "<html><head/><body><p>Saves the position of current points in a file for later use</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exportPoint_btn.setText(QtGui.QApplication.translate("Window", "Save Points", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Window", "<html><head/><body><p>Left click to add a point, Right click to remove a point. </p><p>Points are paried in the order they are created.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearUnmatched_btn.setToolTip(QtGui.QApplication.translate("Window", "Removes points that are not paired on both maps", None, QtGui.QApplication.UnicodeUTF8))
        self.clearUnmatched_btn.setText(QtGui.QApplication.translate("Window", "Clear Unmatched Points", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAll_btn.setToolTip(QtGui.QApplication.translate("Window", "<html><head/><body><p>Removes<span style=\" font-size:12pt; font-weight:600;\"> all points</span> from both maps</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAll_btn.setText(QtGui.QApplication.translate("Window", "Clear ALL Points", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Window", "Number of Points in Map 1: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Window", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Window", "Number of Points in Map 2: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Window", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tools.setTabText(self.tools.indexOf(self.affine_tool), QtGui.QApplication.translate("Window", "Affine", None, QtGui.QApplication.UnicodeUTF8))
        self.importZone_btn.setToolTip(QtGui.QApplication.translate("Window", "Import a zone file to convert points.", None, QtGui.QApplication.UnicodeUTF8))
        self.importZone_btn.setText(QtGui.QApplication.translate("Window", "Import Zone File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Window", "File Preview:", None, QtGui.QApplication.UnicodeUTF8))
        self.zoneData.setDocumentTitle(QtGui.QApplication.translate("Window", "data", None, QtGui.QApplication.UnicodeUTF8))
        self.exportZone_btn.setToolTip(QtGui.QApplication.translate("Window", "Export the converted data points", None, QtGui.QApplication.UnicodeUTF8))
        self.exportZone_btn.setText(QtGui.QApplication.translate("Window", "Export Converted Points", None, QtGui.QApplication.UnicodeUTF8))
        self.tools.setTabText(self.tools.indexOf(self.zone_tool), QtGui.QApplication.translate("Window", "Zones", None, QtGui.QApplication.UnicodeUTF8))
        self.toggleRobot.setText(QtGui.QApplication.translate("Window", "Show Robot", None, QtGui.QApplication.UnicodeUTF8))

from customview import customView

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Window = QtGui.QDialog()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

