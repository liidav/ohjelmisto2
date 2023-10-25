class Hissi:
    def __init__(self, alin, ylin):
        self.alin=alin
        self.ylin=ylin
        self.kerros=alin
    def kerros_ylos(self):
        self.kerros += 1
        print(f'Hissi on nyt kerroksessa {self.kerros}')
    def kerros_alas(self):
        self.kerros -= 1
        print(f'Hissi on nyt kerroksessa {self.kerros}')
    def siirry_kerrokseen(self,krs):
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
            self.hissit.append(Hissi(self.alin, self.ylin))
        print(f'hissejä luotu: {hissien_lkm} kpl')
    def aja_hissia(self, nro, kohde):
        self.hissit[nro].siirry_kerrokseen(kohde)


t1 = Talo(1,5,3)

t1.aja_hissia(1,4)