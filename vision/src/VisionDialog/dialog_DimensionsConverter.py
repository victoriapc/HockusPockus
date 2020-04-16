# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DimensionsConverter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_DimensionsConverter(object):
    def setupUi(self, Dialog_DimensionsConverter):
        Dialog_DimensionsConverter.setObjectName("Dialog_DimensionsConverter")
        Dialog_DimensionsConverter.resize(542, 348)
        self.layoutWidget = QtWidgets.QWidget(Dialog_DimensionsConverter)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 482, 319))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.doubleSpinBox_Height = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_Height.setProperty("value", 0.25)
        self.doubleSpinBox_Height.setObjectName("doubleSpinBox_Height")
        self.horizontalLayout.addWidget(self.doubleSpinBox_Height)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.doubleSpinBox_Width = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_Width.setProperty("value", 0.26)
        self.doubleSpinBox_Width.setObjectName("doubleSpinBox_Width")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_Width)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Retry)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 1)

        self.retranslateUi(Dialog_DimensionsConverter)
        self.buttonBox.rejected.connect(Dialog_DimensionsConverter.reject)
        self.buttonBox.accepted.connect(Dialog_DimensionsConverter.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog_DimensionsConverter)

    def retranslateUi(self, Dialog_DimensionsConverter):
        _translate = QtCore.QCoreApplication.translate
        Dialog_DimensionsConverter.setWindowTitle(_translate("Dialog_DimensionsConverter", "Dialog"))
        self.label.setText(_translate("Dialog_DimensionsConverter", "Please click on each corner of the robot\'s playing area. Start with the bottom left corner, and then click on the top right one. Please also indicate the lengths of each side (default values correspond to the CADs provided on the git repository). When you are done, press Ok. If you wish to start again, press the Retry button. "))
        self.label_2.setText(_translate("Dialog_DimensionsConverter", "Height"))
        self.label_3.setText(_translate("Dialog_DimensionsConverter", "meters"))
        self.label_4.setText(_translate("Dialog_DimensionsConverter", "Width"))
        self.label_5.setText(_translate("Dialog_DimensionsConverter", "meters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_DimensionsConverter = QtWidgets.QDialog()
    ui = Ui_Dialog_DimensionsConverter()
    ui.setupUi(Dialog_DimensionsConverter)
    Dialog_DimensionsConverter.show()
    sys.exit(app.exec_())
