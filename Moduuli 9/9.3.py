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

    def kuje(self, tunnit):
        self.kuljettu_matka += tunnit*self.nopeus_nyt



auto1 = Auto("ABC-123", 142, 60, 2000)

auto1.kuje(1.5)

print(f'{auto1.kuljettu_matka:.0f}')