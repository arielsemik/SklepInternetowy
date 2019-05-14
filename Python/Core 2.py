import pymysql

#####
### Klasa odpowiadająca za łączenie się z bazą danych
#####
class DBConect():
    koszyk_produktow = {}
    def __init__(self):
        self.conn = pymysql.connect('localhost','root', '123456qwerty', 'sklep_internetowy', charset='utf8')


class Klient(DBConect):

    def menu_klienta(self):

        print("MENU KLIENTA")
        akcja = input("-    Wpisz \"1\" aby wyszukać produkty \n-    Wpisz \"2\" aby dokonać zakupu \n-    Wpisz \"3\" aby oczyścić koszyk produktów \n-    Wpisz \"4\" aby zobaczyć status swoich zamówień \n----- Wyjście z programu po wpisaniu \"EXIT\" \n...").strip().upper()

        if akcja == "1":
            self.wyszukiwarka_produktow()
            self.menu_klienta()
        elif akcja == "2":
            self.realizacja_zamowienia(self.email)
            self.menu_klienta()
        elif akcja == "3":
            self.koszyk_produktow.clear()
            self.menu_klienta()

        elif akcja == "4":
            self.kursor = self.conn.cursor()
            self.kursor.execute(R"select id from users where email = '{}'".format(self.email))
            numer_klienta = self.kursor.fetchall()[0][0]
            self.kursor = self.conn.cursor()
            self.kursor.execute(R"select id as 'Numer zamówienia', create_date as 'Data zamówienia', State as 'Status zamówienia'  from order_header where customer = '{}'".format(numer_klienta))
            wszystkie_zamowienia = self.kursor.fetchall()
            print(wszystkie_zamowienia)
            """print("Numer zamówienia       Data zamówienia       Status zamówienia")
            for x in wszystkie_zamowienia:
                zamowienie = wszystkie_zamowienia[x]
                print("{}       {}       {}" .format(zamowienie[0],  zamowienie[1], zamowienie[2]))"""


            self.menu_klienta()
        elif akcja == "EXIT":
            print("Żegnaj :)")
            exit()

    def dodawanie_do_koszyka(self):

        numer_produktu = int(input("Podaj numer produktu, który chcesz dodać do koszyka"))
        while numer_produktu in self.koszyk_produktow.keys():
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nTen produkt zostal już dodany do koszyka\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            numer_produktu = int(input("Podaj poprawny numer produktu, który chcesz dodać do koszyka\n"))
        ilosc = int(input("Ile sztuk dodać do koszyka? \n ... "))
        self.koszyk_produktow[numer_produktu] = ilosc
        print("Produkt o numerze ", numer_produktu, " został dodany do koszyka w numerze. ", ilosc, "\n")
        print("Twój koszyk produktów\n")
        for x in self.koszyk_produktow.keys():
            print("Nazwa produktu: {}     ilość: {}\n".format(x, self.koszyk_produktow[x]))

        #### Dodanie kolejnego produktu
        decyzja = input("Czy chcesz wyszukać kolejny produkt? Wpisz: \n"
                        "D - dodaj kolejny produkt\n"
                        "Z - realizuje zamówienie\n"
                        "C - czyszczę koszyk").strip().upper()
        if decyzja == "D":
            self.wyszukiwarka_produktow()

        elif decyzja == "Z":
            print("Realizacja zamówienia....\n")
            self.realizacja_zamowienia(self.email)

        elif decyzja == "C":
            self.koszyk_produktow.clear()
        else:
            print("Nie zrozumiałem odpowiedzi. Rozpocznij jeszcze raz.")
            self.dodawanie_do_koszyka()
    def realizacja_zamowienia(self, email):

        if len(self.koszyk_produktow) == 0:
            print("Koszyk jest pusty. Wyszukaj produkty, aby je dodać do koszyka...\n")
            self.menu_klienta()

        self.email = email
        ########
        ## Pobranie ID klienta z emaila
        ########

        self.kursor = self.conn.cursor()
        self.kursor.execute(R"select id from users where email = '{}'".format(self.email))
        numer_klienta = self.kursor.fetchall()[0][0]



        ####
        ## Tworzenie nagłówka zamówienia zakupu
        ####
        self.kursor = self.conn.cursor()
        wynik2 =self.kursor.execute(R"INSERT INTO sklep_internetowy.order_header(id,customer) VALUES(null, {})" .format(numer_klienta))
        wynik =self.kursor.fetchall()
        self.conn.commit()
        ####
        ## Pobranie numeru zamowienia
        ####
        self.kursor = self.conn.cursor()
        self.kursor.execute(R"select max(id) from order_header where customer = {}" .format(numer_klienta))
        ostatnie_zamowienie = (self.kursor.fetchall())[0][0]

        ####
        ## Pobranie jednostki z produktu
        ####

        ####
        ##Tworzenie wierszy zamówienia
        ####
        koszyk = self.koszyk_produktow
        for x in koszyk.keys():
            produkt = x
            ilosc = koszyk[x]
            ###
            ##Pobieram jednostkę
            ###
            self.kursor = self.conn.cursor()
            self.kursor.execute("select name_p from products where id = {}" .format(produkt))
            nazwa_p = (self.kursor.fetchall())[0][0]

            self.kursor = self.conn.cursor()
            self.kursor.execute(R"select unit from inventory where product = '{}'" .format(nazwa_p))
            wynik = self.kursor.fetchall()
            wynik = wynik[0][0]

            self.kursor = self.conn.cursor()
            self.kursor.execute(R"INSERT INTO sklep_internetowy.order_lines(id, order_id_fk, product_fk, quantity, unit, State) VALUES(null, {},'{}',{},'{}','Nowe')" .format(ostatnie_zamowienie, nazwa_p, ilosc, wynik))
            wynik = self.kursor.fetchall()
            self.conn.commit()
        print("Zamówienie numer {} zostało utworzone ze statusem 'Nowe'" .format(ostatnie_zamowienie))

    def wyszukiwarka_produktow(self):

        print("Wyszukiwarka produktów")

        #####
        ## Klient wyszukuje produkty w bazie danych
        #####

        szukana_fraza = input("Wprowadź nazwę produktu, którego poszukujesz\n... ")
        szukana_fraza = "%" + szukana_fraza + "%"
        self.kursor = self.conn.cursor()
        self.kursor.execute(r"SELECT id as 'Numer produktu', name_p as 'Nazwa produktu', description_p as 'Opis produktu',price as 'Cena' , quantity as 'Dostępna ilość' FROM sklep_internetowy.products left join inventory on products.name_p = inventory.product where products.name_p like '%s'" % (szukana_fraza))
        wynik = self.kursor.fetchall()

        #####
        ## Ścieżka decyzyjna w zależności od ilości znalezionych produktów produktów
        #####
        if len(wynik) == 0:
            print("Nie znaleźliśmy takiego produktu")
            self.wyszukiwarka_produktow()
        elif len(wynik) == 1:
            op = ['Opis', 'Cena', 'Dostępność']
            print("--------------------------------------")
            print("Znaleźliśmy 1 produkt wg wyszukiwanych kryteriów")
            print("--------------------------------------")
            for produkt in range(len(wynik)):
                print("--------------------------------------")
                # print("       NR {}  {:5s}".format(produkt + 1, wynik[produkt][0]))
                print("--------------------------------------")
                for x in range(len(op)):
                    print("{:30s} {}".format(op[x], wynik[produkt][x + 1]))
                print("--------------------------------------\n")

        elif len(wynik) > 1:
            naglowki = ['Opis', 'Cena', 'Dostępność']
            print("--------------------------------------")
            print("Znaleźliśmy {} {}".format(len(wynik), ["produkty" if len(wynik) < 5 else "produktów"]))

            print("--------------------------------------")
            for produkt in range(len(wynik)):
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("  Numer produktu: {}      {:5}".format(wynik[produkt][0], wynik[produkt][1]))
                print("--------------------------------------")
                for x in range(len(naglowki)):
                    print("{:30s} {}".format(naglowki[x], wynik[produkt][x + 2]))
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

        #### decyzja czy dodać produkt
        decyzja = input("Czy chcesz któryś produkt dodać do koszyka? T/N").strip().upper()
        if decyzja == "T":
            self.dodawanie_do_koszyka()
        else:
            self.menu_klienta()



class Menu(Klient):
    def strona_startowa(self):
        print("Witaj użytkowniku Sklepu internetowego NAJLEPSZY SKLEP INTERNETOWY śWIATA")
        sprawdzenie_klienta = input(
            "-   Wpisz TAK, aby przejść do panelu logowania \n-   Wpisz NIE, aby się zarejestrować \n----- Wyjście z programu po wpisaniu EXIT \n...").strip().upper()

        if sprawdzenie_klienta == 'TAK':
            self.logowanie()
            self.menu_klienta()

        elif sprawdzenie_klienta == 'NIE':
            self.rejestracja_nowego_klienta()
            self.menu_klienta()

        elif sprawdzenie_klienta == 'EXIT':
            print("Żegnaj :)")
            exit()

##### DOPISAĆ OPCJE DLA ADMINA I SPRZEDAWCY

    def logowanie(self):
        """
        Logowanie jako użytkownik
        """

        self.email = input("Podaj email: \n")
        Klient.email = self.email
        haslo = input("Wprowadź hasło: \n")
        self.kursor = self.conn.cursor()
        self.kursor.execute(r"SELECT * FROM sklep_internetowy.users where email = '%s' and pass = '%s'" % (self.email, haslo))
        logowanie = self.kursor.fetchall()
        while len(logowanie) != 1:
            print("Błędny login lub hasło")
            self.email = input("Podaj email: \n")
            haslo = input("Wprowadź hasło: \n")
            self.kursor.execute(r"SELECT * FROM sklep_internetowy.users where email = '%s' and pass = '%s'" % (self.email, haslo))
            logowanie = self.kursor.fetchall()
        print("Zostałeś zalogowany!!!!")

    def rejestracja_nowego_klienta(self):
        print("Witaj na stronie rejestracji\n \n")

        #Stowrzone do testu wprowadzania dannych
        imie = "as"
        nazwisko = "ass"
        self.email = "asaaa@.pl"
        haslo = "asaa"
        nip = 1212
        ulica = "asa 23"
        miasto = 'mmm'
        kod_pocztowy = 22234
        """
        #### Wprowadzenie danych klienta

        imie = input('Podaj swoje imie: \n')
        nazwisko = input("Podaj swoje naziwsko: \n")
        self.email = input("Teraz podaj email: \n")
        self.kursor = self.conn.cursor()
        self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s'" % (self.email))
        istniejacy_klient = self.kursor.fetchall()
        ####Sprawdzenie czy klient jest w bazie
        while len(istniejacy_klient) != 0:
            sprawdzenie = input("Ten email już istnieje w bazie danych czy chcesz zarejestrować nowego klienta?\n TAK - Kontynuuj rejestracje nowego klienta\n NIE - Zakończ rejestracje i przejdź do menu głównego: \n").strip().upper()
            if sprawdzenie == 'TAK':
                email = input("Poda poprawny email: \n")
                self.kursor = self.conn.cursor()
                self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s'" % (email))
                istniejacy_klient = self.kursor.fetchall()
            elif sprawdzenie == 'NIE':
                self.strona_startowa()
            else:
                self.strona_startowa()

        ### Wprowadzenie i sprawdzenie hasła
        haslo = input("wprowadź hasło: \n")
        haslo2 = input("Powtówrz hasło: \n")
        while haslo != haslo2:
            haslo = input("Hasła różnią się od siebie. Wprowadź hasło ponownie: \n")
            haslo2 = input("Powtówrz hasło: \n")
        #### Sprawdzenie czy dodajemy nip
        firma = input('Wpisz Tak jeżeli rejestrujesz się jako firma? Nie - jeżeli osoba fizyczna \n').strip().upper()
        if firma == 'TAK':
            nip = int(input("Wprowadz nip firmy: \n"))
        else:
            nip = 'null'
        adres = input('Wpisz Tak jeżeli chcesz wprowadziić teraz dane adresowe? Nie - jeżeli chcesz je wprowadzić później: \n').strip().upper()
        if adres == 'TAK':
            ulica = input("Wprowadz ulicę i numer: \n")
            miasto = input('Wprowadż nazwę miasta: \n')
            kod_pocztowy = input("Wprowadź kod pocztowy: \n")
        else:
            ulica = 'null'
            miasto = 'null'
            kod_pocztowy = 'null'

        """
        ### Zapisanie w bazie danych nowego klienta
        self.kursor = self.conn.cursor()
        self.kursor.execute("'INSERT INTO sklep_internetowy.users(id,name_u,surname_u,email,tax_number,role_name,street,city,postal_code,pass,create_date) VALUES(null, '%s' ,'%s','%s','%s', 'Customer' ,'%s','%s','%s','%s', null)'" % (
            imie, nazwisko, self.email, nip, ulica, miasto, kod_pocztowy, haslo))

        decyzja = input("Wpisz:\n TAK jeżeli potwierdzasz załozenie konta w sklepie internetowym NAJLEPSZY SKLEP INTERNETOWY śWIATA\n NIE - jeżeli chcesz wrócić do menu głownego \n").strip().upper()

        """ DO POPRAWY, NIE PRZECHODZI W TYM MOMENCIE WARUNEK
        while decyzja != "TAK" or decyzja != "NIE":
            print("Nie rozumiem odpowiedzi")
            decyzja = input("Wpisz:\n TAK jeżeli potwierdzasz załozenie konta w sklepie internetowym NAJLEPSZY SKLEP INTERNETOWY śWIATA\n NIE - jeżeli chcesz wrócić do menu głownego \n").strip().upper()
        """
        print("po decyzji")
        if decyzja == "TAK":
            self.conn.commit()
            print("Witaj w naszym sklepie")
        elif decyzja == "NIE":
            self.conn.rollback()
            print("Dziękujemy, zapraszamy ponownie")
            self.strona_startowa()




ab =Menu()
bc = ab.strona_startowa()
#bc = ab.zakupy('asaaa@.pl')
#bc = ab.wyszukiwarka_produktow()
#bc = ab.manu_klienta()
print(bc)

