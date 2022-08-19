from datetime import datetime
from ssl import CERT_NONE
from bson import ObjectId
from pymongo import MongoClient

class arm_database:
    def __init__(self):
        self._str_url       =  "aui va el sting de coonexion"
        self._mng_clt       =  MongoClient(self._str_url, ssl_cert_reqs=CERT_NONE)
        self._db_refe       = self._mng_clt.get_database("iwanttobuy")
        self._col_carts     = self._db_refe.get_collection("carts")
        self._col_produ     = self._db_refe.get_collection("products")
        self._col_purch     = self._db_refe.get_collection("purchases")
        self._col_users     = self._db_refe.get_collection("users")

    def get_user(self, str_email):
        user_data = self._col_users.find_one({'email': str_email})
        return user_data

    def get_user_cart_linkers(self, str_userid):
        cart_data = self._col_carts.find({'user_id': str_userid}, {'_id': 1, "product_id": 1})
        return list(cart_data)

    def get_user_cart_itemsId(self, str_userid):
        list_cart = self.get_user_cart_linkers(str_userid)
        list_itemsIdstr = []

        for int_i in range(0, len(list_cart)):
            list_itemsIdstr.append(list_cart[int_i]["product_id"])
        return list_itemsIdstr

    def get_user_cart_dictOfRepeatedOcurrences(self, str_userid):
        list_cart = self.get_user_cart_itemsId(str_userid)
        dict_cart = {i: list_cart.count(i) for i in list_cart}
        return dict_cart

    def get_user_cart(self, str_userid):

        linkers = self.get_user_cart_linkers(str_userid)
        str_cart = ""
        int_total = 0

        for item in linkers:
            item_holder = self.get_product(item["product_id"])
            str_cart    =  str_cart + str(item["_id"]) + "," + item_holder["title"] + " " + str(item_holder["price"]) + "\n"
            int_total   = int_total + item_holder["price"]
        return (str_cart, int_total)

    def get_user_dictlistcart(self, str_userid):

        linkers = self.get_user_cart_linkers(str_userid)
        str_cart = []
        int_total = 0

        for item in linkers:
            item_holder = self.get_product(item["product_id"])
            str_cart.append(item_holder)
            int_total   = int_total + item_holder["price"]
        return (str_cart, int_total)


    def get_user_cart_cleanString(self, str_userid):

        dict_cart = self.get_user_cart_dictOfRepeatedOcurrences(str_userid)
        str_cart = ""
        int_total = 0

        for item_key in dict_cart:
            item_holder = self.get_product(item_key)
            str_cart = str_cart + ((item_holder["title"] + " " + str(item_holder["price"]) + "\n") * dict_cart[item_key])
            int_total = int_total + (item_holder["price"] * dict_cart[item_key])
        return (str_cart, int_total)

    def purchase_user_cart(self, str_userid):

        str_list, int_price = self.get_user_cart(str_userid)

        if str_list == "":
            print("Incompleto")
            return False

        strlist_itemStandAlone = str_list.split("\n")
        strlist_itemStandAlone.pop()

        strlist_itemIdStandAlone = []
        str_list = ""

        for int_i in range(0,len(strlist_itemStandAlone)):
            itemId_itemPlusPrice = strlist_itemStandAlone[int_i].split(",")

            if len(itemId_itemPlusPrice) > 1: #La ultima iteracion estara con un elemento vacio.
                strlist_itemIdStandAlone.append(itemId_itemPlusPrice[0])
                strlist_itemStandAlone[int_i] = itemId_itemPlusPrice[1]
                str_list = str_list + strlist_itemStandAlone[int_i] + "\n"


        self._col_purch.insert_one({'date': datetime.now(), 'list': str_list, 'price': int_price, 'user_id': str_userid, '__v': 0})
        return True

    def deplete_user_cart(self, str_userid):
        self._col_carts.delete_many({'user_id': str_userid})

    def complete_purchase(self, str_userid):
        if self.purchase_user_cart(str_userid):
            self.deplete_user_cart(str_userid)

    def get_product(self, str_itemId):
        prod_data = self._col_produ.find_one({'_id': ObjectId(str_itemId)})
        return prod_data

    def get_all_products(self):
        return list(self._col_produ.find())

    def get_all_purchased_products(self):
        return list(self._col_purch.find())

    def add_product_to_user_cart(self, str_itemId, str_userid):
        self._col_carts.insert_one({"product_id" : str(str_itemId), "user_id" : str(str_userid), "__v": 0})

    def add_product_to_user_cart_complete(self, str_itemId, str_userid):
        if self.get_product(str_itemId) is not None:
            self.add_product_to_user_cart(str_itemId, str_userid)
        else:
            print("Operacion invalida")

    def remove_product_to_user_cart(self, index_id):
        self._col_carts.delete_one({'_id': ObjectId(index_id)})

    def remove_product_to_user_cart_complete(self, str_product_id, str_user_id):

        if self._col_carts.find_one({'product_id': str_product_id, 'user_id': str_user_id}) is not None:
            self._col_carts.delete_one({'product_id': str_product_id, 'user_id': str_user_id})
        else:
            print("Operacion invalida")
