
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus_nyt += nopeuden_muutos
        if self.nopeus_nyt < 0:
            self.nopeus_nyt = 0
        elif self.nopeus_nyt > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus


auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f'{auto1.nopeus_nyt} km/h')

auto1.kiihdyta(-200)

print(f'{auto1.nopeus_nyt} km/h')