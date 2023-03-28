from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()      #self._rutenett blir laget av _lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):           #returnerer en nøsted liste laget av liste1 og _lag_tom_rad()
        liste1 = [] 
        for i in range(self._ant_rader):
            liste1.append(self._lag_tom_rad())
        return liste1

    def _lag_tom_rad(self):
        liste2 = []
        for i in range(self._ant_kolonner):
            liste2.append(None)
        return liste2

    def fyll_med_tilfeldige_celler(self):   #brukes i gen 1. Lager et tilfeldig sett med celler i rutenett.
        for i1 in range(self._ant_rader):    
            for i2 in range(self._ant_kolonner): 
                n = randint(0,1)
                if (n == 0) and (i1 < self._ant_rader and i2 < self._ant_kolonner):
                    self.lag_celle(i1, i2)
                    self._rutenett[i1][i2].sett_levende()
                elif (n == 1 or n == 2) and (i1 < self._ant_rader and i2 < self._ant_kolonner):
                    self.lag_celle(i1, i2)
                    self._rutenett[i1][i2].sett_doed()

    def lag_celle(self, rad, kol):
        self._rutenett[rad][kol] = Celle()

    def hent_celle(self, rad, kol): #returnerer cellen med parameter som blir brukt som indeks for rad og kol
        if rad in range(0,len(self._rutenett)) and kol in range(0, len(self._rutenett[rad])):
            return self._rutenett[rad][kol]
        else:
            return None

    def tegn_rutenett(self):    #teger rutenett i terminalen. Ved \n og end="" begynner ikke hver print på ny linje
        for e in self._rutenett:
            print("\n", end="")
            for e2 in e:
                print(f"{e2.hent_status_tegn()}", end="")

    def _sett_naboer(self, rad, kol):
        _main_celle = self._rutenett[rad][kol]  #cellen som blir sjekket er definert her som _main_celle
        for e in range(-1,2):  #for-løkke definerer e som første indeks i rutenett som 1 over rad, rad og 1 under rad.
            for e2 in range(-1,2):  #for-løkke definerer e2 som andre indeks i rutenett, med 1 til venstre for _main_celle, _main_celle og 1 til høyre for _main_celle.              
                _celle = self.hent_celle(rad+e, kol+e2)
                if (_celle != None) and (_celle != _main_celle):
                    _main_celle.legg_til_nabo(_celle)

    def koble_celler(self): #bruker _sett_naboer for hver indeks i rutenett
        for i1 in range(self._ant_rader):
            for i2 in range(self._ant_kolonner):
                i2 += 1
                if self.hent_celle(i1, i2) != None:
                    self._sett_naboer(i1, i2)

    def hent_alle_celler(self):
        liste = []
        for e in self._rutenett:
            for e2 in e:
                if e2 != None:
                    liste.append(e2)
        return liste

    def antall_levende(self):
        _antall_levende_celler = 0
        for e in self._rutenett:
            for e2 in e:
                if (e2 != None) and (e2.er_levende()):
                    _antall_levende_celler += 1
        return _antall_levende_celler

    def hoved_metode(self): #egendefinert metode som gjør det enkelt å kjøre metoder i hovedprogram.py
        self.fyll_med_tilfeldige_celler()
        self.koble_celler()
        return self