"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
"""

class Hissi:
    def __init__(self, alin, ylin, nro):
        self.alin=alin
        self.ylin=ylin
        self.nro=nro
        self.kerros=alin
    def kerros_ylos(self):
        self.kerros += 1
        print(f'Hissi {self.nro} on nyt kerroksessa {self.kerros}')
    def kerros_alas(self):
        self.kerros -= 1
        print(f'Hissi {self.nro} on nyt kerroksessa {self.kerros}')
    def siirry_kerrokseen(self, krs):
        while krs != self.kerros:
            if krs > self.kerros:
                self.kerros_ylos()
            elif krs < self.kerros:
                self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissien_lkm = hissien_lkm
        self.hissit = []
        for x in range (0,self.hissien_lkm):
            self.hissit.append(Hissi(alin, ylin, x))

    def aja_hissia(self, nro, kohde):
        self.hissit[nro].siirry_kerrokseen(kohde)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


t1 = Talo(1,5,3)

t1.aja_hissia(2,5)
t1.aja_hissia(1,4)
t1.aja_hissia(0,3)

t1.palohalytys()