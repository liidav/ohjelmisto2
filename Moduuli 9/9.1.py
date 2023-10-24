class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka


auto1 = Auto("ABC-123", 142)

ominaisuudet = vars(auto1)
for i in ominaisuudet:
    print(f"{i}: {ominaisuudet[i]}")
