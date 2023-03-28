from random import randint

class SauSprite:
    def __init__(self, bilde, pvenstre, ptopp, listeGress):
        self._bilde = bilde
        self._pvenstre = pvenstre
        self._ptopp = ptopp
        self._fart_fra_venstre = 1
        self._fart_fra_topp = 1
        self._er_spist = False
        self._liste_gress = listeGress
    def blir_spist(self):
        self._er_spist = True
    def er_spist(self):
        return self._er_spist
    def sett_posisjon(self, x, y):
        self._pvenstre = x
        self._ptopp = y
    def hent_pvenstre(self):
        return self._pvenstre
    def hent_ptopp(self):
        return self._ptopp
    def hent_fart_fra_venstre(self):
        return self._fart_fra_venstre
    def hent_fart_fra_topp(self):
        return self._fart_fra_topp
    def sett_fart(self, x, y):
        self._fart_fra_venstre = x
        self._fart_fra_topp = y
    def beveg(self):
        self.n1 = randint(0,200)
        self.n2 = randint(0,200)
        self._pvenstre += self._fart_fra_venstre
        if self._pvenstre == 850 or self.n1 == 20:
            self._fart_fra_venstre = -(self._fart_fra_venstre)
        elif self._pvenstre == 0 or self.n1 == 1:
            self._fart_fra_venstre = -(self._fart_fra_venstre)
        self._ptopp += self._fart_fra_topp
        if self._ptopp == 650 or self.n2 == 20:
            self._fart_fra_topp = -(self._fart_fra_topp)
        elif self._ptopp == 0 or self.n2 == 1:
            self._fart_fra_topp = -(self._fart_fra_topp)   
    def snu(self):
        self._fart_fra_venstre = -(self._fart_fra_venstre)
        self._fart_fra_topp = -(self._fart_fra_topp)
    def tegn(self, skjerm):
        if self._er_spist != True:
            skjerm.blit(self._bilde, (self._pvenstre, self._ptopp))
    def finn_naermeste_gress(self):
        k01 = self.hent_pvenstre()- self._liste_gress[0].hent_pvenstre()
        k02 = self.hent_ptopp() - self._liste_gress[0].hent_ptopp()
        hyp01 = (k01**2 + k02**2)**0.5
        naermesteGress = self._liste_gress[0]
        for e in self.liste_med_gress:
            if e.er_spist() == False:
                k1 = self.hent_pvenstre()- e.hent_pvenstre()
                k2 = self.hent_ptopp() - e.hent_ptopp()
                hyp = (k1**2 + k2**2)**0.5
                if hyp < hyp01:
                    hyp = hyp01
                    naermesteGress = e
        return naermesteGress