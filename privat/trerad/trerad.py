

from random import randint

class Nummer():
    def __init__(self):
        self._verdi = 0
    
    def sett_verdi(self, verdi):
        self._verdi = verdi


class Brett():
    def __init__(self):
        self._l1 = []
        self._nummer_liste = [1,2,3,4,5,6,7,8,9]

    def pros1(self, antall_rader, antall_kolonner):
        for i in range(antall_rader):
            self._l1.append(self.pros2(antall_kolonner))
            
    def pros2(self, x):
        for i in range(x):
            self._l2 = []
            num = Nummer()
            self._l2.append(num)
        return self._l2

    def pros3(self):
        index = -1
        for i1 in self._l1:
            index += 1
            for i2 in i1:
                self.hent_verdi(i2)
    
    def hent_verdi(self, celle):
        int = randint(0,9)
        if int not in self._nummer_liste:
            self.hent_verdi(celle)
        else:
            self._nummer_liste.remove(int)
            celle.sett_verdi(int)

    def print_brett(self):
        for index in range(len(self._l1)):
            for i2 in self._l1[index]:
                print(f"{self.hent_verdi(i2)}", end="")
        

brett = Brett()
brett.pros1(3,3)
brett.pros3()
brett.print_brett()