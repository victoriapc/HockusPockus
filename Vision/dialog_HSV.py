# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_HSV.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_HSV(object):
    def setupUi(self, Dialog_HSV):
        Dialog_HSV.setObjectName("Dialog_HSV")
        Dialog_HSV.resize(637, 418)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_HSV)
        self.buttonBox.setGeometry(QtCore.QRect(240, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog_HSV)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 79, 484, 200))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_2)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalSlider_blue = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_blue.setMaximum(255)
        self.horizontalSlider_blue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_blue.setObjectName("horizontalSlider_blue")
        self.verticalLayout_2.addWidget(self.horizontalSlider_blue)
        self.label_H = QtWidgets.QLabel(self.frame_2)
        self.label_H.setObjectName("label_H")
        self.verticalLayout_2.addWidget(self.label_H)
        self.horizontalSlider_green = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_green.setMaximum(255)
        self.horizontalSlider_green.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_green.setObjectName("horizontalSlider_green")
        self.verticalLayout_2.addWidget(self.horizontalSlider_green)
        self.label_S = QtWidgets.QLabel(self.frame_2)
        self.label_S.setObjectName("label_S")
        self.verticalLayout_2.addWidget(self.label_S)
        self.horizontalSlider_red = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_red.setMaximum(255)
        self.horizontalSlider_red.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_red.setObjectName("horizontalSlider_red")
        self.verticalLayout_2.addWidget(self.horizontalSlider_red)
        self.label_V = QtWidgets.QLabel(self.frame_2)
        self.label_V.setObjectName("label_V")
        self.verticalLayout_2.addWidget(self.label_V)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog_HSV)
        self.buttonBox.accepted.connect(Dialog_HSV.accept)
        self.buttonBox.rejected.connect(Dialog_HSV.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_HSV)

    def retranslateUi(self, Dialog_HSV):
        _translate = QtCore.QCoreApplication.translate
        Dialog_HSV.setWindowTitle(_translate("Dialog_HSV", "Dialog"))
        self.label_title.setText(_translate("Dialog_HSV", "HSV Color Values"))
        self.label_H.setText(_translate("Dialog_HSV", "H"))
        self.label_S.setText(_translate("Dialog_HSV", "S"))
        self.label_V.setText(_translate("Dialog_HSV", "V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_HSV = QtWidgets.QDialog()
    ui = Ui_Dialog_HSV()
    ui.setupUi(Dialog_HSV)
    Dialog_HSV.show()
    sys.exit(app.exec_())
