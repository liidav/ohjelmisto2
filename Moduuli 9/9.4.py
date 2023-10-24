import random
from tabulate import tabulate
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

kisa = True

while kisa:
    for auto in autot:
        kiihdytys = random.randint(-10,15)
        auto.kiihdyta(kiihdytys)
        auto.kulje(1)
    for auto in autot:
        if auto.kuljettu_matka >= 1000:
            kisa = False

all_data = [["Rekisteritunnus", "Kuljettu matka", "Huippunopeus", "Loppunopeus"], [], [], [], [], [], [], [], [], [], []]

for x in range (1,11):
    all_data[x].append(autot[x-1].rekisteritunnus)
    all_data[x].append(autot[x-1].kuljettu_matka)
    all_data[x].append(autot[x-1].huippunopeus)
    all_data[x].append(autot[x - 1].nopeus_nyt)

taulukko = tabulate(all_data,headers='firstrow')

print(taulukko)