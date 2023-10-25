class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        for avain, arvo in vars(self).items():
            print(f'{avain}: {arvo}')

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        for avain, arvo in vars(self).items():
            print(f'{avain}: {arvo}')

l1 = Lehti("Aku Ankka", "Aki Hyyppä")
k1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

k1.tulosta_tiedot()
l1.tulosta_tiedot()
