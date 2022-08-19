import bcrypt

class obj_users:

    def __init__(self):
        self._str_email     =  ""
        self._str_password  =  b""
        self._str_userid    =  ""

    def login(self, dict_user, str_password):
        if dict_user == None:
            print("No existe tal correo.")
            return False
        self._str_email     =  dict_user["email"]
        self._str_password  =  str.encode(dict_user["password"])
        if bcrypt.checkpw(str_password, self._str_password):
            self._str_userid = str(dict_user["_id"])
            return True
        else:
            print("Contraseña no coincide.")
            return False

    def get_str_userID(self):
        return self._str_userid

