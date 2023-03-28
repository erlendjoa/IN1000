from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._rutenett = self._rutenett.hoved_metode()  #egendefinert metode i rutenett.py
        self._generasjonsnummer = 0
    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f"\n\nGen: {self._generasjonsnummer}\nAnt: {self._rutenett.antall_levende()}")
    def oppdatering(self):
        spsm = input("Trykke enter for å fortsette: ")
        while spsm != "q":
            for i in self._rutenett.hent_alle_celler():
                i.tell_levende_naboer()
            for i in self._rutenett.hent_alle_celler():
                i.oppdater_status()
            self._generasjonsnummer += 1
            self.tegn()
            spsm = input("Trykke enter for å fortsette: ")