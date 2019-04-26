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
    if firma == 'TAK':
        nip = int(input("Wprowadz nip firmy: \n"))
    else:
        nip = 'null'

    adres = input(
        'Wpisz Tak jeżeli chcesz wprowadziić teraz dane adresowe? Nie - jeżeli chcesz je wprowadzić później: \n').strip().upper()
    if adres == 'TAK':
        ulica = input("Wprowadz ulicę i numer: \n")
        miasto = input('Wprowadż nazwę miasta: \n')
        kod_pocztowy = input("Wprowadź kod pocztowy: \n")
    else:
        ulica = 'null'
        miasto = 'null'
        kod_pocztowy = 'null'

    DBConect.kursor.execute("INSERT INTO `sklep_internetowy`.`users`(`id`,`name_u`,`surname_u`,`email`,`tax_number`,`role_name`,`street`,`city`,`postal_code`,`pass`,`create_date`) VALUES( null, %s ,%s,%s>,%s>, 'Customer' ,%s,%s,%s>,%s, null)" % (
        imie, nazwisko, email, nip, ulica, miasto, kod_pocztowy, haslo))
    decyzja = input("Wpisz TAK jeżeli potwierdzasz załozenie konta w sklepie internetowym NAJLEPSZY SKLEP INTERNETOWY śWIATA\n Lub wpisz Nie jeżelichcesz wrócić do menu głownego \n").strip().upper()
    while decyzja != 'TAK' or decyzja == 'NIE':
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