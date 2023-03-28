
class Sau():
    def __init__(self, posisjon, navn):
        self._posisjon = posisjon
        self._navn = navn
        self._lever = True
    def blir_spist(self):
        self._lever = False
    def lever(self):
        if self._lever == True:
            return True
        else:
            return False
    def hent_navn(self):
        return self._navn
    def hent_posisjon(self):
        return self._posisjon

class Ulv():
    def __init__(self, posisjon, navn):
        self._posisjon = posisjon
        self._navn = navn
        self.vekt = 20
    def spis_sau(self, sau):
        sau.blir_spist()
        self.vekt += 5
    def hent_vekt(self):
        return self.vekt
    def hent_navn(self):
        return self._navn
    def hent_posisjon(self):
        return self._posisjon
    def beveg_hoyre(self):
        if self._posisjon > 10:
            self._posisjon = 1
        else:
            self._posisjon += 1
    def beveg_venstre(self):
        if self._posisjon < 1:
            self._posisjon = 10
        self._posisjon -= 1