#Oppgave 3.


class Hund:         #1. Her har jeg definert class Hund og definert noen instansvariabler som oppgitt i oppgavetekst.
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10
    def hent_alder(self):
        return self.alder
    def hent_vekt(self):
        return self.vekt
    def spring(self):       #4. Metoden spring reduserer metthet med 1. og Når metthet er mindre enn 5 vil den også redusere vekt med 1
        self.metthet -= 1
        if self.vekt > 5:
            self.vekt -= 1
    def spis(self, mengde):
        mengde += self.metthet
        if self.metthet > 7:
            self.vekt += 1