# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnlogin = QPushButton(self.centralwidget)
        self.btnlogin.setObjectName(u"btnlogin")
        self.btnlogin.setGeometry(QRect(350, 300, 100, 25))
        self.txtemail = QLineEdit(self.centralwidget)
        self.txtemail.setObjectName(u"txtemail")
        self.txtemail.setGeometry(QRect(350, 200, 150, 25))
        self.txtpassword = QLineEdit(self.centralwidget)
        self.txtpassword.setObjectName(u"txtpassword")
        self.txtpassword.setGeometry(QRect(350, 250, 150, 25))
        self.lblemail = QLabel(self.centralwidget)
        self.lblemail.setObjectName(u"lblemail")
        self.lblemail.setEnabled(True)
        self.lblemail.setGeometry(QRect(200, 200, 36, 16))
        self.lblpassword = QLabel(self.centralwidget)
        self.lblpassword.setObjectName(u"lblpassword")
        self.lblpassword.setGeometry(QRect(200, 250, 55, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnlogin.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.lblemail.setText(QCoreApplication.translate("MainWindow", u"email:", None))
        self.lblpassword.setText(QCoreApplication.translate("MainWindow", u"password", None))
    # retranslateUi

