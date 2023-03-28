class Stein:
    def __init__(self, bilde, pvenstre, ptopp):
        self._bilde = bilde
        self._pvenstre = pvenstre
        self._ptopp = ptopp
        self._er_spist = False
    def blir_spist(self):
        self._er_spist = True
    def er_spist(self):
        return self._er_spist
    def hent_pvenstre(self):
        return self._pvenstre
    def hent_ptopp(self):
        return self._ptopp
    def tegn(self, skjerm):
        skjerm.blit(self._bilde, (self._pvenstre, self._ptopp))