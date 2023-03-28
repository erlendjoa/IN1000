#Oppgave 1.

#1. Her har jeg opprettet en class med navn Motorsykkel, og definert en instantsvariabel for total km. 

class Motorsykkel:
    def __init__(self, merke, nummer):
        self.tot_km = 0
        self.merke = merke
        self.nummer = nummer
    def kjor(self, ny_km):          #2. Her har jeg definert metoden kjor, som øker kilometersavstand med parameter ny_km.
        self.tot_km += ny_km
    def hent_kilometerstand(self):  #3. Return metode som hetner totale kilometeren.
        return self.tot_km
    def skriv_ut(self):
        print(f"Merke: {self.merke}, Nummer: {self.nummer}, Avstand: {self.tot_km}km.")
    