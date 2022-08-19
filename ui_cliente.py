# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_addproduct = QPushButton(self.centralwidget)
        self.btn_addproduct.setObjectName(u"btn_addproduct")
        self.btn_addproduct.setGeometry(QRect(600, 145, 100, 25))
        self.table_items = QTableWidget(self.centralwidget)
        if (self.table_items.columnCount() < 3):
            self.table_items.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_items.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_items.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_items.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_items.setObjectName(u"table_items")
        self.table_items.setGeometry(QRect(20, 20, 550, 150))
        self.table_cart = QTableWidget(self.centralwidget)
        if (self.table_cart.columnCount() < 3):
            self.table_cart.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_cart.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_cart.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_cart.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.table_cart.setObjectName(u"table_cart")
        self.table_cart.setGeometry(QRect(20, 200, 550, 150))
        self.table_purchase = QTableWidget(self.centralwidget)
        if (self.table_purchase.columnCount() < 3):
            self.table_purchase.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_purchase.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_purchase.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_purchase.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.table_purchase.setObjectName(u"table_purchase")
        self.table_purchase.setGeometry(QRect(20, 380, 550, 150))
        self.btn_purchase = QPushButton(self.centralwidget)
        self.btn_purchase.setObjectName(u"btn_purchase")
        self.btn_purchase.setGeometry(QRect(600, 325, 100, 25))
        self.btn_removeproduct = QPushButton(self.centralwidget)
        self.btn_removeproduct.setObjectName(u"btn_removeproduct")
        self.btn_removeproduct.setGeometry(QRect(600, 280, 100, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 200, 55, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(600, 240, 175, 25))
        self.lbl_iditem = QLabel(self.centralwidget)
        self.lbl_iditem.setObjectName(u"lbl_iditem")
        self.lbl_iditem.setGeometry(QRect(600, 30, 55, 16))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(600, 70, 175, 25))
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
        self.btn_addproduct.setText(QCoreApplication.translate("MainWindow", u"agregar", None))
        ___qtablewidgetitem = self.table_items.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.table_items.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.table_items.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem3 = self.table_cart.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem4 = self.table_cart.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem5 = self.table_cart.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem6 = self.table_purchase.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem7 = self.table_purchase.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem8 = self.table_purchase.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.btn_purchase.setText(QCoreApplication.translate("MainWindow", u"comprar", None))
        self.btn_removeproduct.setText(QCoreApplication.translate("MainWindow", u"remover", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id_Inciso", None))
        self.lbl_iditem.setText(QCoreApplication.translate("MainWindow", u"Id_producto", None))
    # retranslateUi

