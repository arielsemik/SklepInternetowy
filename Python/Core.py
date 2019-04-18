
import pymysql



class DBConect:
    def __init__(self):
        self.conn = pymysql.connect('localhost','root', '123456qwerty', 'sklep_internetowy', charset='utf8')

    def wyswietlenie_userow(self):
        self.kursor = self.conn.cursor()
        self.kursor.execute("select * from users")
        wyniki = self.kursor.fetchall()
        print(wyniki)



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
        print("Nie rozumiem Twojej odpowiedzi. Zacznijmy jeszcze raz")
        strona_startowa()


class PanelKlienta():
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


        """
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
