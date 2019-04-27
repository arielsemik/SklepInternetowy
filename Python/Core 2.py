
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

    def strona_startowa(self):
        print("Witaj użytkowniku Sklepu internetowego NAJLEPSZY SKLEP INTERNETOWY śWIATA")
        sprawdzenie_klienta = input("-   Wpisz TAK, aby przejść do panelu logowania \n-   Wpisz NIE, aby się zarejestrować \n----- Wyjście z programu po wpisaniu EXIT \n...").strip().upper()

        if sprawdzenie_klienta == 'TAK':
            self.logowanie()
        elif sprawdzenie_klienta == 'NIE':
            self.rejestracja_nowego_klienta()
        elif sprawdzenie_klienta == "EXIT":
            print("Żegnaj :)")
            exit()
    def manu_klienta(self):
        print("MENU KLIENTA")
        akcja = input("-   Wpisz \"1\" aby wyszukać produkty \n-   Wpisz \"2\" aby dokonać zakupu \n----- Wyjście z programu po wpisaniu \"EXIT\" \n...").strip().upper()

        if akcja == "1":
            self.wyszukiwarka_produktow()
        elif akcja == "2":
            self.zakupy()
        elif akcja == "EXIT":
            print("Żegnaj :)")
            exit()

    def wyszukiwarka_produktow(self):
        koszyk_produktow = []

        print("Witaj w wyszukiwarce produktów")
        #####
        ## Klient wyszukuje produkty w bazie danych
        #####
        szukana_fraza = input("Wprowadź nazwę produktu, ktorego poszukujesz\n... ")
        szukana_fraza = "%"+szukana_fraza+"%"
        self.kursor = self.conn.cursor()
        self.kursor.execute('SELECT name_p as "Nazwa produktu", description_p as "Opis produktu",price as "Cena" , quantity as "Dostępna ilość" FROM sklep_internetowy.products left join inventory on products.name_p = inventory.product where products.name_p like %s', (szukana_fraza))
        wynik = self.kursor.fetchall()
        print(wynik)
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
                print("       NR {}  {:5s}".format(produkt + 1, wynik[produkt][0]))
                print("--------------------------------------")
                for x in range(len(op)):
                    print("{:30s} {}".format(op[x], wynik[produkt][x + 1]))
                print("--------------------------------------\n")
            decyzja = input("Czy chcesz ten produkt dodać do  koszyka? T/N").strip().upper()
            if decyzja =="T":
                koszyk_produktow.append("do skonczenia")
            elif decyzja == "N":
                print("OK, wracasz do menu klienta")
                self.manu_klienta()
            else:
                print("Nie rozumiem odpowiedzi, wracasz do menu klienta")
                self.manu_klienta()
        elif len(wynik) > 1:
            naglowki = ['Opis', 'Cena', 'Dostępność']
            print("--------------------------------------")
            print("Znaleźliśmy {} {}" .format(len(wynik), ["produkty" if len(wynik)<5 else "produktów"]))
            print("--------------------------------------")
            for produkt in range(len(wynik)):
                print("--------------------------------------")
                print("       NR {}  {:5s}" .format(produkt +1 ,wynik[produkt][0]))
                print("--------------------------------------")
                for x in range(len(naglowki)):
                    print("{:30s} {}" .format(naglowki[x], wynik[produkt][x+1]))
                print("--------------------------------------\n")
            decyzja = input("Czy chcesz któryś produkt dodać do koszyka? T/N").strip().upper()
            if decyzja == "T":
                decyzja = int(input("Podaj numer produktu, który chcesz dodać do koszyka"))
                koszyk_produktow.append("do skonczenia")
            elif decyzja == "N":
                print("OK, wracasz do menu klienta")
                self.manu_klienta()
            else:
                print("Nie rozumiem odpowiedzi, wracasz do menu klienta")
                self.manu_klienta()
            )


    def logowanie(self):
        """
        Logowanie jako użytkownik
        """

        email = input("Podaj email: \n")
        haslo = input("Wprowadź hasło: \n")
        self.kursor = self.conn.cursor()
        self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s' and pass = '%s'" % (email, haslo))
        logowanie = self.kursor.fetchall()
        print(len(logowanie))
        while len(logowanie) != 1:
            print("Błędny login lub hasło")
            email = input("Podaj email: \n")
            haslo = input("Wprowadź hasło: \n")
            self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s' and pass = '%s'" % (email, haslo))
            logowanie = self.kursoretchall()
        print("Zostałeś zalogowany!!!!")

    def rejestracja_nowego_klienta(self):
        print("Witaj na stronie rejestracji\n \n")
        imie = "as"
        nazwisko = "ass"
        email = "asaaa@.pl"
        haslo = "asaa"
        nip = 1212
        ulica = "asa 23"
        miasto = 'mmm'
        kod_pocztowy = 22234
        """
        #### Wprowadzenie danych klienta
        
        imie = input('Podaj swoje imie: \n')
        nazwisko = input("Podaj swoje naziwsko: \n")
        email = input("Teraz podaj email: \n")
        self.kursor = self.conn.cursor()
        self.kursor.execute("SELECT * FROM sklep_internetowy.users where email = '%s'" % (email))
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
        self.kursor.execute("INSERT INTO `sklep_internetowy`.`users`(`id`,`name_u`,`surname_u`,`email`,`tax_number`,`role_name`,`street`,`city`,`postal_code`,`pass`,`create_date`) VALUES(null, '%s' ,'%s','%s','%s', 'Customer' ,'%s','%s','%s','%s', null)" % (imie, nazwisko, email, nip, ulica, miasto, kod_pocztowy, haslo))

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

    def zakupy(self):
        email = self.logowanie(email)

        ####
        ## Pobranie ID klienta z emaila
        ####
        self.kursor = self.conn.cursor()
        self.kursor.execute("select id from users where email = %s", (email))
        numer_klienta = self.kursor.fetchall()
        numer = numer_klienta[0][0]

        ####
        ## Tworzenie nagłówka zamówienia zakupu
        ####
        self.kursor = self.conn.cursor()
        wynik2 =self.kursor.execute("INSERT INTO sklep_internetowy.order_header(id,customer) VALUES(null, %s)", numer)
        wynik =self.kursor.fetchall()
        self.conn.commit()
        ####
        ## Pobranie numeru zamowienia
        ####
        self.kursor = self.conn.cursor()
        self.kursor.execute("select max(id) from order_header where customer = %s", (numer))
        ostatnie_zamowienie = (self.kursor.fetchall())[0][0]

        print(ostatnie_zamowienie)

"""
"""
ab =DBConect()
#bc = ab.strona_startowa()
#bc = ab.zakupy('asaaa@.pl')
bc = ab.wyszukiwarka_produktow()
#bc = ab.manu_klienta()
print(bc)

