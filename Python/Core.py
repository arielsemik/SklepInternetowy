
import pymysql


class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password


class Seller(User):
    def __init__(self, name, surname, email, password, role_name = 'Seller'):
        super().__init__(name, surname, email, password)
        self.role_name = role_name

class Customer(User):
    def __init__(self, name, surname, email, password, role_name = 'Customer'):
        super().__init__(name, surname, email, password)
        self.role_name = role_name

class Admin(User):
    def __init__(self, name, surname, email, password, role_name = 'Admin'):
        super().__init__(name, surname, email, password)
        self.role_name = role_name


MySQL structure