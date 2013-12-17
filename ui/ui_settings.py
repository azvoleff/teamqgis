# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_settings.ui'
#
# Created: Tue Dec 17 10:30:44 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(314, 210)
        self.gridLayout = QtGui.QGridLayout(Settings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_2 = QtGui.QFrame(Settings)
        self.frame_2.setMinimumSize(QtCore.QSize(281, 24))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 41, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(150, 0, 35, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.yres = QtGui.QDoubleSpinBox(self.frame_2)
        self.yres.setGeometry(QtCore.QRect(190, 0, 91, 22))
        self.yres.setDecimals(4)
        self.yres.setMinimum(0.0)
        self.yres.setMaximum(600.0)
        self.yres.setProperty("value", 30.0)
        self.yres.setObjectName(_fromUtf8("yres"))
        self.xres = QtGui.QDoubleSpinBox(self.frame_2)
        self.xres.setGeometry(QtCore.QRect(40, 0, 91, 22))
        self.xres.setDecimals(4)
        self.xres.setMinimum(0.0)
        self.xres.setMaximum(600.0)
        self.xres.setProperty("value", 30.0)
        self.xres.setObjectName(_fromUtf8("xres"))
        self.gridLayout.addWidget(self.frame_2, 5, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Settings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.saveSelectionInProject = QtGui.QCheckBox(Settings)
        self.saveSelectionInProject.setChecked(True)
        self.saveSelectionInProject.setObjectName(_fromUtf8("saveSelectionInProject"))
        self.gridLayout.addWidget(self.saveSelectionInProject, 1, 0, 1, 1)
        self.rubberWidth = QtGui.QDoubleSpinBox(Settings)
        self.rubberWidth.setToolTip(_fromUtf8(""))
        self.rubberWidth.setDecimals(1)
        self.rubberWidth.setSingleStep(1.0)
        self.rubberWidth.setProperty("value", 2.0)
        self.rubberWidth.setObjectName(_fromUtf8("rubberWidth"))
        self.gridLayout.addWidget(self.rubberWidth, 3, 1, 1, 1)
        self.scale = QtGui.QSpinBox(Settings)
        self.scale.setMinimum(1)
        self.scale.setMaximum(50)
        self.scale.setProperty("value", 5)
        self.scale.setObjectName(_fromUtf8("scale"))
        self.gridLayout.addWidget(self.scale, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Settings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Settings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.dockArea = QtGui.QComboBox(Settings)
        self.dockArea.setObjectName(_fromUtf8("dockArea"))
        self.dockArea.addItem(_fromUtf8(""))
        self.dockArea.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.dockArea, 0, 1, 1, 1)
        self.useDualView = QtGui.QCheckBox(Settings)
        self.useDualView.setObjectName(_fromUtf8("useDualView"))
        self.gridLayout.addWidget(self.useDualView, 1, 1, 1, 1)
        self.frame = QtGui.QFrame(Settings)
        self.frame.setMinimumSize(QtCore.QSize(296, 32))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.rubberColor = QtGui.QLabel(self.frame)
        self.rubberColor.setGeometry(QtCore.QRect(151, 0, 144, 21))
        self.rubberColor.setMinimumSize(QtCore.QSize(144, 21))
        self.rubberColor.setText(_fromUtf8(""))
        self.rubberColor.setObjectName(_fromUtf8("rubberColor"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 145, 21))
        self.label.setMinimumSize(QtCore.QSize(145, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.frame, 4, 0, 1, 2)

        self.retranslateUi(Settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "teamtraining :: settings", None))
        self.label_5.setText(_translate("Settings", "X shift", None))
        self.label_6.setText(_translate("Settings", "Y shift", None))
        self.label_2.setText(_translate("Settings", "Rubberband size", None))
        self.saveSelectionInProject.setText(_translate("Settings", "save selection in project", None))
        self.label_3.setText(_translate("Settings", "Scaling", None))
        self.label_4.setText(_translate("Settings", "Dock area", None))
        self.dockArea.setItemText(0, _translate("Settings", "left", None))
        self.dockArea.setItemText(1, _translate("Settings", "right", None))
        self.useDualView.setText(_translate("Settings", "use dual view", None))
        self.label.setText(_translate("Settings", "Rubberband color", None))

