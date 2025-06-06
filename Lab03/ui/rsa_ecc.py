# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rsa_ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_message = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_message.setGeometry(QtCore.QRect(190, 130, 771, 121))
        self.txt_message.setPlaceholderText("")
        self.txt_message.setObjectName("txt_message")
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(190, 270, 771, 151))
        self.txt_signature.setPlaceholderText("")
        self.txt_signature.setObjectName("txt_signature")
        self.btn_gen_key_rsa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_key_rsa.setGeometry(QtCore.QRect(250, 490, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_gen_key_rsa.setFont(font)
        self.btn_gen_key_rsa.setObjectName("btn_gen_key_rsa")
        self.btn_sign_rsa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign_rsa.setGeometry(QtCore.QRect(480, 490, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_sign_rsa.setFont(font)
        self.btn_sign_rsa.setObjectName("btn_sign_rsa")
        self.btn_verify_rsa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify_rsa.setGeometry(QtCore.QRect(740, 490, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_verify_rsa.setFont(font)
        self.btn_verify_rsa.setObjectName("btn_verify_rsa")
        self.lbl_result_rsa = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_rsa.setGeometry(QtCore.QRect(490, 460, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_result_rsa.setFont(font)
        self.lbl_result_rsa.setObjectName("lbl_result_rsa")
        self.btn_gen_key_ecc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_key_ecc.setGeometry(QtCore.QRect(250, 640, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_gen_key_ecc.setFont(font)
        self.btn_gen_key_ecc.setObjectName("btn_gen_key_ecc")
        self.btn_sign_ecc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign_ecc.setGeometry(QtCore.QRect(490, 640, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_sign_ecc.setFont(font)
        self.btn_sign_ecc.setObjectName("btn_sign_ecc")
        self.btn_verify_ecc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify_ecc.setGeometry(QtCore.QRect(740, 650, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_verify_ecc.setFont(font)
        self.btn_verify_ecc.setObjectName("btn_verify_ecc")
        self.lbl_result_ecc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_ecc.setGeometry(QtCore.QRect(500, 600, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_result_ecc.setFont(font)
        self.lbl_result_ecc.setObjectName("lbl_result_ecc")
        self.lbl_result_rsa_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_rsa_2.setGeometry(QtCore.QRect(370, 10, 411, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_result_rsa_2.setFont(font)
        self.lbl_result_rsa_2.setObjectName("lbl_result_rsa_2")
        self.lbl_result_rsa_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_rsa_3.setGeometry(QtCore.QRect(30, 130, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_result_rsa_3.setFont(font)
        self.lbl_result_rsa_3.setObjectName("lbl_result_rsa_3")
        self.lbl_result_rsa_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_rsa_4.setGeometry(QtCore.QRect(30, 270, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_result_rsa_4.setFont(font)
        self.lbl_result_rsa_4.setObjectName("lbl_result_rsa_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ký số và xác minh (RSA & ECC)"))
        self.btn_gen_key_rsa.setText(_translate("MainWindow", "Generate Keys"))
        self.btn_sign_rsa.setText(_translate("MainWindow", "Sign"))
        self.btn_verify_rsa.setText(_translate("MainWindow", "Verify"))
        self.lbl_result_rsa.setText(_translate("MainWindow", "Kết quả RSA"))
        self.btn_gen_key_ecc.setText(_translate("MainWindow", "Generate Keys"))
        self.btn_sign_ecc.setText(_translate("MainWindow", "Sign"))
        self.btn_verify_ecc.setText(_translate("MainWindow", "Verify"))
        self.lbl_result_ecc.setText(_translate("MainWindow", "Kết quả ECC"))
        self.lbl_result_rsa_2.setText(_translate("MainWindow", "RSA_ECC Cipher"))
        self.lbl_result_rsa_3.setText(_translate("MainWindow", "Infomation:"))
        self.lbl_result_rsa_4.setText(_translate("MainWindow", "Signature:"))
