from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QGraphicsScene, QTableWidgetItem
from ui_cliente import Ui_MainWindow
from arm_mongo import *
from user import *

class MainWindow(QMainWindow):
    def __init__(self, str_userID):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.database = arm_database()
        self.str_userID = str_userID
        self.load_product_table()
        self.load_cart_table()
        self.load_purchase_table()

        self.ui.btn_addproduct.clicked.connect(self.add_product_to_cart)
        self.ui.btn_removeproduct.clicked.connect(self.remove_product_from_cart)
        self.ui.btn_purchase.clicked.connect(self.purchase)

    def add_product_to_cart(self):
        arm_database().add_product_to_user_cart_complete(self.ui.lineEdit_2.text(), self.str_userID)
        self.load_cart_table()

    def remove_product_from_cart(self):
        arm_database().remove_product_to_user_cart_complete(self.ui.lineEdit.text(), self.str_userID)
        self.load_cart_table()

    def purchase(self):
        arm_database().complete_purchase(self.str_userID)
        self.load_purchase_table()
        self.load_cart_table()

    def load_product_table(self):
        data_holder = self.database.get_all_products()
        self.ui.table_items.setRowCount(len(data_holder))
        row = 0
        for item in data_holder:
            self.ui.table_items.setItem(row, 0, QTableWidgetItem(str(item["_id"])))
            self.ui.table_items.setItem(row, 1, QTableWidgetItem(str(item["title"])))
            self.ui.table_items.setItem(row, 2, QTableWidgetItem(str(item["price"])))
            row = row + 1

    def load_cart_table(self):
        data_holder = self.database.get_user_dictlistcart(self.str_userID)[0]
        self.ui.table_cart.setRowCount(len(data_holder))
        row = 0
        print(data_holder)
        for item in data_holder:

            self.ui.table_cart.setItem(row, 0, QTableWidgetItem(str(item["_id"])))
            self.ui.table_cart.setItem(row, 1, QTableWidgetItem(str(item["title"])))
            self.ui.table_cart.setItem(row, 2, QTableWidgetItem(str(item["price"])))
            row = row + 1

    def load_purchase_table(self):
        data_holder = self.database.get_all_purchased_products()
        self.ui.table_purchase.setRowCount(len(data_holder))
        row = 0
        for item in data_holder:

            self.ui.table_purchase.setItem(row, 0, QTableWidgetItem(str(item["_id"])))
            self.ui.table_purchase.setItem(row, 1, QTableWidgetItem(str(item["list"])))
            self.ui.table_purchase.setItem(row, 2, QTableWidgetItem(str(item["price"])))
            row = row + 1