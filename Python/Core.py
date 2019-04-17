
import pymysql



class DBConect:
    def __init__(self):
        self.conn = pymysql.connect('localhost','root', '123456qwerty', 'sklep_internetowy', charset='utf8')

    def wyswietlenie_userow(self):
        self.kursor = self.conn.cursor()
        self.kursor.execute("select * from users")
        wyniki = self.kursor.fetchall()
        print(wyniki)

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
class MenuGlowne():
    def strona_startowa(self):
        print("Witaj użytkowniku Sklepu internetowego NAJLEPSZY SKLEP INTERNETOWY śWIATA")
        sprawdzenie_klienta = input("Czy jesteś już naszym klientem? \n Wpisz TAK, aby przejść do panelu logowania \n Wpisz NIE, aby się zarejestrować \n lub wprowadz tajny kod pracownika Admin/Seller. \n \n Wyjście z programu zawsze po wpisaniu EXIT")
        sprawdzenie_klienta = sprawdzenie_klienta.strip()

    if sprawdzenie_klienta.upper() == 'TAK':

    elif sprawdzenie_klienta.upper() == 'NIE':

    elif sprawdzenie_klienta.upper() == 'ADMIN':

    elif sprawdzenie_klienta.upper() == 'SELLER':

    elif sprawdzenie_klienta.upper() == 'EXIT':
        print("Dziękujemy że odwiedzileś naszą witrynę.")

    else:
        print("Nie rozumiem Twojej odpowiedzi.")


class PanelKlienta():
    def rejestracja_nowego_klienta(self):


    def aktualizacja_danych_klienta(self):


    def wyswietlanie_produktow(self):

    def zamawianie(self):

    def zwroty(self):

    def sprawdzenie_statusu zamowienia()

class PanelAdmina():
    def dodawanie_userow(self):


class PanelSprzedawcy():
    def dodawanie_produktów(self):

    def dodawanie_produktow_na_stan(self):

    def realizacja_zamowienia
sprawdzeniepolaczenia = DBConect()
