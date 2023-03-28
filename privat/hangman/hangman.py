

class Hangman:
    def __init__(self):
        self._ord = []
        self._f = []

    def sett_ord(self):
        self._riktig_ord = input("Skriv inn ord: ")
        for i in self._riktig_ord:
            self._ord.append(i)
            self._f.append("_")

    def beregn_streng(self):
        for i in self._f:
            print(f"{i} ",end="")

    def gjette_pros(self):
        self._gjett_ord = input(f"{self.beregn_streng()}  |  Gjett ord eller bokstav: ")
        self._g = self._gjett_ord.split()
        for e in self._g:
            if e in self._ord:
                for i in self._g:
                    index = -1
                    for i2 in self._ord:   
                        index += 1
                        if i == i2:
                            self._f[index] = f"{i}"
        if self._gjett_ord.lower() != self._riktig_ord.lower():
            self.gjette_pros()
        else:
            print(f"Du vant. Ordet var {self._riktig_ord}")

            
        
hangman = Hangman()
hangman.sett_ord()
hangman.gjette_pros()