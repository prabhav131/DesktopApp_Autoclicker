# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email_sent_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_email_sent_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 159)
        self.enter_key = QtWidgets.QPushButton(Dialog)
        self.enter_key.setGeometry(QtCore.QRect(180, 107, 75, 23))
        self.enter_key.setObjectName("enter_key")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 31))
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 231, 31))
        self.label_4.setText("")
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 371, 31))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enter_key.setText(_translate("Dialog", "Resend"))
        self.label.setText(_translate("Dialog", "Verification email sent to:"))
        self.label_2.setText(_translate("Dialog", "Please click on the link received on email to finish verification. \n"
"Click on resend button below if the verification link has expired."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
