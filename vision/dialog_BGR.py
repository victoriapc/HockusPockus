# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_BGR.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_BGR(object):
    def setupUi(self, Dialog_BGR):
        Dialog_BGR.setObjectName("Dialog_BGR")
        Dialog_BGR.resize(637, 418)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_BGR)
        self.buttonBox.setGeometry(QtCore.QRect(240, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog_BGR)
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
        self.label_blue = QtWidgets.QLabel(self.frame_2)
        self.label_blue.setObjectName("label_blue")
        self.verticalLayout_2.addWidget(self.label_blue)
        self.horizontalSlider_green = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_green.setMaximum(255)
        self.horizontalSlider_green.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_green.setObjectName("horizontalSlider_green")
        self.verticalLayout_2.addWidget(self.horizontalSlider_green)
        self.label_green = QtWidgets.QLabel(self.frame_2)
        self.label_green.setObjectName("label_green")
        self.verticalLayout_2.addWidget(self.label_green)
        self.horizontalSlider_red = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_red.setMaximum(255)
        self.horizontalSlider_red.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_red.setObjectName("horizontalSlider_red")
        self.verticalLayout_2.addWidget(self.horizontalSlider_red)
        self.label_red = QtWidgets.QLabel(self.frame_2)
        self.label_red.setObjectName("label_red")
        self.verticalLayout_2.addWidget(self.label_red)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog_BGR)
        self.buttonBox.accepted.connect(Dialog_BGR.accept)
        self.buttonBox.rejected.connect(Dialog_BGR.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_BGR)

    def retranslateUi(self, Dialog_BGR):
        _translate = QtCore.QCoreApplication.translate
        Dialog_BGR.setWindowTitle(_translate("Dialog_BGR", "Dialog"))
        self.label_title.setText(_translate("Dialog_BGR", "Blue, green and red minimum values"))
        self.label_blue.setText(_translate("Dialog_BGR", "Blue"))
        self.label_green.setText(_translate("Dialog_BGR", "Green"))
        self.label_red.setText(_translate("Dialog_BGR", "Red"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_BGR = QtWidgets.QDialog()
    ui = Ui_Dialog_BGR()
    ui.setupUi(Dialog_BGR)
    Dialog_BGR.show()
    sys.exit(app.exec_())
