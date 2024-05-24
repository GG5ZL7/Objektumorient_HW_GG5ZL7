import datetime

class FelhasznaloiFelulet:
    def __init__(self, szalloda):
        self.szalloda = szalloda

    def menu_megjelenitese(self):
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

    def foglalas(self):
        print("\nFoglalás készítése")
        szobaszam = input("Kérem adja meg a szobaszámot: ")
        datum = input("Kérem adja meg a foglalás dátumát (YYYY-MM-DD): ")

        try:
            datum_obj = datetime.datetime.strptime(datum, "%Y-%m-%d")
            if datum_obj < datetime.datetime.now():
                print("Hiba: A foglalás dátuma nem lehet múltbeli!")
                return
        except ValueError:
            print("Hiba: Érvénytelen dátum formátum!")
            return
        
        foglalhato = False
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalhato = True
                break
 
        if not foglalhato:
            print("Hiba: A megadott szobaszám nem létezik!")
            return      

        foglalas = self.szalloda.foglalas(szobaszam, datum)
        if foglalas:
            print("Foglalás sikeresen létrehozva. Szoba ára:", foglalas.ar)

    def lemondas(self):
        print("\nLemondás")
        szobaszam = input("Kérem adja meg a szobaszámot: ")
        datum = input("Kérem adja meg a foglalás dátumát (YYYY-MM-DD): ")

        talalat = False
        for foglalas in Foglalas.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                talalat = True
                Foglalas.foglalas_leadasa_torlese(foglalas) # hiba: statikus metódus hívása
                print("Foglalás sikeresen lemondva!")
                break

        if not talalat:
            print("Hiba: A megadott foglalás nem található!")

    def listazas(self):
        print("\nFoglalások listája")
        if Foglalas.foglalasok:
            for foglalas in Foglalas.foglalasok:
                print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.ar}")
        else:
            print("Nincsenek foglalások.")

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)  # Egyágyas szoba ára: 10,000 Ft

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Kétágyas szoba ára: 15,000 Ft

class Foglalas:
    foglalasok = []

    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum
        self.ar = szoba.ar
        Foglalas.foglalasok.append(self)

    @staticmethod
    def foglalas_leadasa_torlese(foglalas):
        Foglalas.foglalasok.remove(foglalas)

    @staticmethod
    def foglalasok_listazasa():
        for foglalas in Foglalas.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.ar}")

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas
        return None

# Szobák, szálloda és foglalások inicializálása
egyagyas_szoba1 = EgyagyasSzoba("101")
egyagyas_szoba2 = EgyagyasSzoba("102")
ketagyas_szoba1 = KetagyasSzoba("201")
ketagyas_szoba2 = KetagyasSzoba("202")
ketagyas_szoba3 = KetagyasSzoba("203")

szalloda = Szalloda("Sárvári Hotel")
szalloda.szoba_hozzaadasa(egyagyas_szoba1)
szalloda.szoba_hozzaadasa(egyagyas_szoba2)
szalloda.szoba_hozzaadasa(ketagyas_szoba1)
szalloda.szoba_hozzaadasa(ketagyas_szoba2)
szalloda.szoba_hozzaadasa(ketagyas_szoba3)

Foglalas(szalloda.szobak[0], "2024-05-01")
Foglalas(szalloda.szobak[1], "2024-05-03")
Foglalas(szalloda.szobak[2], "2024-05-05")
Foglalas(szalloda.szobak[3], "2024-05-07")
Foglalas(szalloda.szobak[4], "2024-05-09")

# Felhasználói felület inicializálása
felhasznaloi_felulet = FelhasznaloiFelulet(szalloda)

# Felhasználói interakciók
while True:
    felhasznaloi_felulet.menu_megjelenitese()
    valasztas = input("Kérem adja meg a választott művelet számát: ")

    if valasztas == "1":
        felhasznaloi_felulet.foglalas()
    elif valasztas == "2":
        felhasznaloi_felulet.lemondas()
    elif valasztas == "3":
        felhasznaloi_felulet.listazas()
    elif valasztas == "4":
        print("Kilépés...")
        break
    else:
        print("Hiba: Érvénytelen választás!")
