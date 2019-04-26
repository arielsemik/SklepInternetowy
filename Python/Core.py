
import pymysql


#####
### Klasa odpowiadająca za łączenie się z bazą danych
#####
class DBConect:
    def __init__(self):
        self.conn = pymysql.connect('localhost','root', '123456qwerty', 'sklep_internetowy', charset='utf8')

    def wyswietlenie_userow(self):
        self.kursor = self.conn.cursor()
        self.kursor.execute("select * from users")
        wyniki = self.kursor.fetchall()
        print(wyniki)

######
### Klasa która będzie menu głównym użytkownika, nie odbywa się tu łączenie z bazą danych tylko sprawdzeniez jakim użytkownikiem mamy do czynienia: Sprzedawca, klient, admin
######


class MenuGlowne:
    def strona_startowa(self):
        print("Witaj użytkowniku Sklepu internetowego NAJLEPSZY SKLEP INTERNETOWY śWIATA")
        sprawdzenie_klienta = input("Czy jesteś już naszym klientem? \n - Wpisz TAK, aby przejść do panelu logowania \n - Wpisz NIE, aby się zarejestrować \n - Wprowadz tajny kod pracownika Admin/Seller. \n ----- Wyjście z programu po wpisaniu EXIT \n").strip().upper()

        if sprawdzenie_klienta == 'TAK':
           PanelKlienta.logowanie_klienta()

       # elif sprawdzenie_klienta == 'NIE':

"""
        elif sprawdzenie_klienta == 'ADMIN':

        elif sprawdzenie_klienta == 'SELLER':

        elif sprawdzenie_klienta == 'EXIT':
            print("Dziękujemy że odwiedzileś naszą witrynę.")

        else:
            print("Nie rozumiem Twojej odpowiedzi. Zacznijmy jeszcze raz")
            strona_startowa()

"""
class PanelKlienta():

    def manu_klienta(self):
        wybor_menu_klienta = int(input("Wybierz: \n1 - Katalog produktów \n2 - Zamów produkty \n3 - Sprawdź postęp realizacji zamówienia \n4 - Zmień swoje dane"))
     #   if wybor_menu_klienta == 1:

 #       elif wybor_menu_klienta == 2:

 #       elif wybor_menu_klienta == 3:

  #      elif wybor_menu_klienta == 4:


    def logowanie_klienta(self):
        print("Witaj nasz ulubiony kliencie sklepu internetowego NAJLEPSZY SKLEP INTERNETOWY śWIATA")
        email = input("Podaj email: \n")
        haslo = input("Wprowadź hasło: \n")
        self.kursor = self.conn.cursor()
        self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s' and pass = '%s'" %(email,haslo))
        logowanie = self.kursor.fetchall()
        while len(logowanie) != 1:
            print("Błędny login lub hasło")
            email = input("Podaj email: \n")
            haslo = input("Wprowadź hasło: \n")
            self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s' and pass = '%s'" % (email, haslo))
            logowanie = self.kursor.fetchall()

        print("Zostałeś zalogowany!!!!")
     #   self.manu_klienta()
"""
        imieklienta = "SELECT name_u FROM sklep_internetowy.users where email = %s and pass = %s"
        print("Zostałeś zalogowany! Witaj %s !", imieklienta)
    def katalog_produktow(self):
        DBConect.kursor.execute("SELECT * FROM sklep_internetowy.products left join inventory on products.name_p = inventory.product")
        PanelKlienta.manu_klienta()

    def tworzenie_zamowienia(self):
        "''INSERT INTO `sklep_internetowy`.`order_header`(`customer`, `street_order`, `city_order`, `postal_code_order`, `street_invoice`, `city_invoice`,`postal_code_invoice`, `tax_number`, `create_date`, `State`, `order_date`, `sent_date`) VALUES
        (% s,)
        ''"
        wyszukiwana_nazwa = input("Wprowadź frazę lub pełną nazwę produktu, którego poszukujesz")
        wyszukany_produkt = DBConect.kursor.execute("SELECT id as \"Numer produktu\", name_p as \"Nazwa produktu\" , price as \"Cena\" FROM `sklep_internetowy`.`products`where products.name_p like %s", wyszukiwana_nazwa)

        if wyszukany_produkt.count > 1:
            print("Istnieje więcej niż jeden produktów o tej nazwie")

            for produkt in wyszukany_produkt:
                print(produkt)

            wybor_produktu = input("Wybierz numer produktu do zamówienia")

            wyszukany_produkt = DBConect.kursor.execute("SELECT * FROM `sklep_internetowy`.`products`where products.id like %s", int(wybor_produktu))
            if wyszukany_produkt.count = 1:

        elif wyszukany_produkt.count == 0:
            print("Produkt nie znaleziony")
            PanelKlienta.tworzenie_zamowienia()
        else:





    def rejestracja_nowego_klienta(self, DBConect, MenuGlowne):
        print("Witaj na stronie logowania \n \n")

        imie = input('Podaj swoje imie: \n')
        nazwisko = input("Podaj swoje naziwsko: \n")
        email = input("Teraz podaj email: \n")
        haslo = input("wprowadź hasło: \n")
        haslo2 = input("Powtówrz hasło: \n")
        while haslo != haslo2:
            haslo = input("Hasła różnią się od siebie. Wprowadź hasło ponownie: \n")
            haslo2 = input("Powtówrz hasło: \n")

        firma = input('Wpisz Tak jeżeli rejestrujesz się jako firma? Nie - jeżeli osoba fizyczna \n').strip().upper()
        if  firma == 'TAK':
            nip = int(input("Wprowadz nip firmy: \n"))
        else:
            nip = 'null'

        adres = input('Wpisz Tak jeżeli chcesz wprowadziić teraz dane adresowe? Nie - jeżeli chcesz je wprowadzić później: \n').strip().upper()
        if  adres == 'TAK':
            ulica = input("Wprowadz ulicę i numer: \n")
            miasto =input('Wprowadż nazwę miasta: \n')
            kod_pocztowy = input("Wprowadź kod pocztowy: \n")
        else:
            ulica = 'null'
            miasto = 'null'
            kod_pocztowy ='null'

        DBConect.kursor.execute("INSERT INTO `sklep_internetowy`.`users`(`id`,`name_u`,`surname_u`,`email`,`tax_number`,`role_name`,`street`,`city`,`postal_code`,`pass`,`create_date`) VALUES( null, %s ,%s,%s>,%s>, 'Customer' ,%s,%s,%s>,%s, null)" %(imie,nazwisko, email,nip, ulica, miasto, kod_pocztowy, haslo))
        decyzja = input("Wpisz TAK jeżeli potwierdzasz załozenie konta w sklepie internetowym NAJLEPSZY SKLEP INTERNETOWY śWIATA\n Lub wpisz Nie jeżelichcesz wrócić do menu głownego \n").strip().upper()
        while decyzja != 'TAK' or decyzja=='NIE':
            DBConect.conn.rollback()
            print("Nie rozumiem odpowiedzi")
            decyzja = input("Wpisz TAK jeżeli potwierdzasz załozenie konta w sklepie internetowym NAJLEPSZY SKLEP INTERNETOWY śWIATA\n Lub wpisz Nie jeżelichcesz wrócić do menu głownego \n").strip().upper()

        if decyzja == "TAK":
            DBConect.conn.commit()
            print("Witaj w naszym sklepie")
            MenuGlowne.strona_startowa()
        elif decyzja == "NIE":
            DBConect.conn.rollback()
            MenuGlowne.strona_startowa()
        PanelKlienta.menu_klienta()


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
        """
sprawdzeniepolaczenia = DBConect()
MenuGlowne.strona_startowa(None)