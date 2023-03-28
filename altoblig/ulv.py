from random import randint

class Ulv:
    def __init__(self, bilde, pvenstre, ptopp, listeSauer, listeSteiner):
        self._bilde = bilde
        self._pvenstre = pvenstre
        self._ptopp = ptopp
        self._fart_fra_venstre = -1
        self._fart_fra_topp = -1
        self._er_spist = False
        self._liste_sauer = listeSauer
        self._liste_steiner = listeSteiner
    def blir_spist(self):
        self._er_spist = True
    def er_spist(self):
        return self._er_spist
    def hent_pvenstre(self):
        return self._pvenstre
    def hent_ptopp(self):
        return self._ptopp
    def hent_fart_fra_venstre(self):
        return self._fart_fra_venstre
    def hent_fart_fra_topp(self):
        return self._fart_fra_topp
    def beveg(self):
        sau = self.finn_naermeste_sau()
        if sau.hent_pvenstre() < self._pvenstre:
            self._fart_fra_venstre = -1
        elif sau.hent_pvenstre() > self._pvenstre:
            self._fart_fra_venstre = 1
        if sau.hent_ptopp() < self._ptopp:
            self._fart_fra_topp = -1
        elif sau.hent_ptopp() > self._ptopp:
            self._fart_fra_topp = 1


        self._pvenstre += self._fart_fra_venstre
        if self._pvenstre >= 850:
            self.snu()
        elif self._pvenstre == 0 :
            self.snu()
        self._ptopp += self._fart_fra_topp
        if self._ptopp >= 650:
            self.snu()
        elif self._ptopp == 0:
            self.snu()
    def snu(self):
        self._fart_fra_venstre = self._fart_fra_venstre*-1
        self._fart_fra_topp = self._fart_fra_topp*-1
    def tegn(self, skjerm):
        skjerm.blit(self._bilde, (self._pvenstre, self._ptopp))
    def finn_naermeste_sau(self):
        k01 = self.hent_pvenstre()- self._liste_sauer[0].hent_pvenstre()
        k02 = self.hent_ptopp() - self._liste_sauer[0].hent_ptopp()
        hyp01 = (k01**2 + k02**2)**0.5
        naermesteSau = self._liste_sauer[0]
        for e in self._liste_sauer:
            if e.er_spist() == False:
                k1 = self.hent_pvenstre()- e.hent_pvenstre()
                k2 = self.hent_ptopp() - e.hent_ptopp()
                hyp = (k1**2 + k2**2)**0.5
                if hyp < hyp01:
                    hyp = hyp01
                    naermesteSau = e
        return naermesteSau