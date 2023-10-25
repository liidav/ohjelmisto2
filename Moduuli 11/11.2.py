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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

s1 = Sahkoauto("ABC-15", 180, 52.5)
p1 = Polttomoottoriauto("ACD-123", 165, 32.3)

s1.kiihdyta(95)
p1.kiihdyta(87)

s1.kulje(3)
p1.kulje(3)

print(f'Sähköauton matkamittarin lukema: {s1.kuljettu_matka}')
print(f'Polttomoottoriauton matkamittarin lukema: {p1.kuljettu_matka}')