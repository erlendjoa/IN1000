from sauImg import SauSprite
from gress import Gress
from ulv import Ulv
from stein import Stein

class Spillbrett:
    def __init__(self):
        self._sauer = []
        self._gress = []
        self._steiner = []
        self._ulver = []
    def hent_sauer(self):
        return self._sauer
    def hent_steiner(self):
        return self._steiner
    def hent_gress(self):
        return self._gress
    def opprett_sau(self, navn, bilde, pv, pt, lgrs):
        navn = SauSprite(bilde, pv, pt, lgrs)
        self._sauer.append(navn)
    def opprett_gress(self, navn, bilde, pv, pt):
        navn = Gress(bilde, pv, pt)
        self._gress.append(navn)
    def opprett_stein(self, navn, bilde, pv, pt):
        navn = Stein(bilde, pv, pt)
        self._steiner.append(navn)
    def opprett_ulver(self, navn, bilde, pv, pt, lsau, lstn):
        navn = Ulv(bilde, pv, pt, lsau, lstn)
        self._ulver.append(navn)
    def oppdater(self):
        for e in self._sauer:
            e.beveg()
            for e2 in self._gress:
                if har_kollidert(e, e2):
                    e2.blir_spist()
        for e in self._ulver:
            e.beveg()
            for e2 in self._sauer:
                if har_kollidert(e, e2):
                    e2.blir_spist()
    def tegn(self, skjerm):
        for e in self._sauer:
            if e.er_spist() == False:
                e.tegn(skjerm)
        for e in self._gress:
            if e.er_spist() == False:
                e.tegn(skjerm)
        for e in self._steiner:
            e.tegn(skjerm)
        for e in self._ulver:
            e.tegn(skjerm)
def har_kollidert(objekt1, objekt2):
        if (objekt1.hent_pvenstre() > objekt2.hent_pvenstre()-50 and objekt1.hent_pvenstre() < objekt2.hent_pvenstre()+50) and (objekt1.hent_ptopp() > objekt2.hent_ptopp()-50 and objekt1.hent_ptopp() < objekt2.hent_ptopp()+50):
            return True
        else:
            return False