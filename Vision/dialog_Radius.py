# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_Radius.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Radius(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 310)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 50, 351, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_radius = QtWidgets.QLabel(self.frame)
        self.label_radius.setGeometry(QtCore.QRect(100, 20, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_radius.setFont(font)
        self.label_radius.setObjectName("label_radius")
        self.horizontalSlider_radius = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_radius.setGeometry(QtCore.QRect(10, 50, 331, 22))
        self.horizontalSlider_radius.setMaximum(250)
        self.horizontalSlider_radius.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_radius.setObjectName("horizontalSlider_radius")
        self.labe_radius_value = QtWidgets.QLabel(self.frame)
        self.labe_radius_value.setGeometry(QtCore.QRect(20, 80, 81, 20))
        self.labe_radius_value.setObjectName("labe_radius_value")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_radius.setText(_translate("Dialog", "Radius of circle"))
        self.labe_radius_value.setText(_translate("Dialog", "Radius value "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
