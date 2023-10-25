import random
from tabulate import tabulate

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdyta(kiihdytys)
            auto.kulje(1)

    def tulosta_tilanne(self):
        self.all_data = [["Rekisteritunnus", "Kuljettu matka", "Huippunopeus", "Tämänhetkinen nopeus"]]
        for x in range(0,len(self.osallistujat)):
            self.all_data.append([self.osallistujat[x].rekisteritunnus, self.osallistujat[x].kuljettu_matka, self.osallistujat[x].huippunopeus, self.osallistujat[x].nopeus_nyt])

        taulukko = tabulate(self.all_data, headers='firstrow')
        print(taulukko)
    def kilpailu_ohi(self):
        kisaohi = False
        for auto in self.osallistujat:
            if auto.kuljettu_matka >= self.pituus:
                kisaohi = True
        return kisaohi
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus_nyt += nopeuden_muutos
        if self.nopeus_nyt < 0:
            self.nopeus_nyt = 0
        elif self.nopeus_nyt > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit*self.nopeus_nyt

autot = []

for x in range(1,11):
    huippunopeus = random.randint(100,200)
    autot.append(Auto(f"ABC-{x}", huippunopeus))

k1 = Kilpailu("Suuri Romuralli", 8000, autot)

kisakaynnissa = True

while kisakaynnissa:
    for x in range (0,10):
        k1.tunti_kuluu()
        onko_ohi = k1.kilpailu_ohi()
        if onko_ohi == True:
            kisakaynnissa = False
            break
    if kisakaynnissa == True:
        print("\nTILANNEKATSAUS")
        k1.tulosta_tilanne()

print("\nKILPAILU ON PÄÄTTYNYT")
k1.tulosta_tilanne()