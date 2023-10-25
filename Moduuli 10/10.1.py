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

h1 = Hissi(1,6)

h1.siirry_kerrokseen(4)

h1.siirry_kerrokseen(1)


