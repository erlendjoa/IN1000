#Oppgave 4.

class Dato:     #1. Definering av klassen Dato og instantsvariabler
    def __init__(self, ny_dag, ny_maaned, nytt_aar):
        self.ny_dag = ny_dag
        self.ny_maaned = ny_maaned
        self.nytt_aar = nytt_aar
    def hent_aar(self):             #3. Utvidelse av metoder gitt i oppgavetekst
        return self.nytt_aar
    def hent_alt(self):
        return f"{self.ny_dag}.{self.ny_maaned} {self.nytt_aar}"
    def sjekk_dato(self):
        if self.ny_dag == 15:
            return True
        elif self.ny_dag == 1:
            return 1