class Sang():
    def __init__(self, artist, tittel):     #Definerer konstruør med artist og tittel som parametere
        self.tittel = tittel                #Definerer instantsvariabler
        self.artist = artist
    def spill(self):
        print(f"info om {self.tittel} og {self.artist}")        #printer f streng som gitt i oppgavetekst
    def hent_artist(self):
        return self.artist
    def hent_tittel(self):
        return self.tittel
    def sjekk_artist(self, navn):
        l1 = navn.split(" ")                                #Lager lister med split() funksjon. dermed sjekker element i l1 og de er i l2.
        l2 = self.artist.split(" ")
        for e in l1:
            if e in l2:
                return True
        return False
    def sjekk_tittel(self, tittel):
        return tittel.lower() == self.tittel.lower()
    def sjekk_artist_og_tittel(self, artist, tittel):
        return self.sjekk_artist(artist) and self.sjekk_tittel(tittel)
    def __str__(self):
        return self.artist
    def __eq__(self, other):
        return self.artist == other.artist
