from random import randint
from sau import Sau
from sau import Ulv

class Verden:
    def __init__(self):
        self._sauer = []
        self._ulver = []
    def opprett_dyr(self, type, navn, posisjon):
        if type == ("Sau"):
            navn = Sau(posisjon, navn)
            self._sauer.append(navn)
        elif type == ("Ulv"):
            navn = Ulv(posisjon, navn)
            self._ulver.append(navn)
    def beskriv(self):
        for e in self._sauer:
            print(f"{e.hent_navn()}, {e.hent_posisjon()}")
        for e in self._ulver:
            print(f"{e.hent_navn()}, {e.hent_posisjon()}")
    def antall_sauer(self):
        return len(self._sauer)
    def antall_ulver(self):
        return len(self._ulver)
    def oppdaterer(self):
        for e in self._ulver:
            nummer = randint(0,1)
            if nummer == 1:
                e.beveg_hoyre()
            elif nummer == 0:
                e.beveg_venstre()
            for e2 in self._sauer:
                if e.hent_posisjon() == e2.hent_posisjon():
                    e.spis_sau(e2)
                    print(f"Ulven {e.hent_navn()} spiser sauen {e2.hent_navn()} på posisjon {e.hent_posisjon()}.")
    def finn_feiteste_ulv(self):
        s = self._ulver[0]
        v = self._ulver[0].hent_vekt()
        for e in self._ulver:
            if e.hent_vekt() > v:
                v = e.hent_vekt()
                s = e
        return s.hent_navn()

        