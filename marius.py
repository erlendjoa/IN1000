from random import randint

# Challenge fra Marius

class Vannmelom():
    def __init__(self):
        self._froe_liste = [Froe(), Froe(), Froe(), Froe(), Froe(), Froe(), Froe(), Froe(), Froe(), Froe()]


class Froe():
    def __init__(self):
        self._lever = False

        int = randint(0,100)
        if int <= 65:
            self._lever = True
    
    def gro(self):
        if self._lever == True:
            meloner_liste.append(Vannmelom())


meloner_liste = []
froe_liste = []
for i in range(10):
    froe_liste.append(Froe())


aar = input("Skriv inn aar: ")

for i in range(int(aar)):
    for froe in froe_liste:
        froe.gro()


print(len(meloner_liste))
