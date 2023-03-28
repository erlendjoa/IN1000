

class Rett():
    def __init__(self, navn, pris, innholdsliste):
        self._navn = navn
        self._pris = pris
        self._innholdsliste = innholdsliste
    
    def sjekkInnholdOK(self, innholdsstoffer):
        for innhold in innholdsstoffer:
            if innhold in self._innholdsliste:
                return False
        return True

    def __str__(self):
        return f"{self._navn}, {self._pris}, {self._innholdsliste}"

class Kategori():
    def __init__(self, kategorinavn, retter):
        self._kategorinavn = kategorinavn
        self._retter = retter
    
    def hentOKRetter(self, innholdsstoffer):
        ny_liste = []
        for rett in self._retter:
            if rett.sjekkInnholdOK(innholdsstoffer):
                ny_liste.append(rett)
        return ny_liste

    def skrivUtRetter(self):
        print(f"Til {self._kategorinavn}: ")
        for rett in self._retter:
            print(rett)

class Meny():
    def __init__(self, kategorier):
        self._meny = {}
        for kat in kategorier:
            kat_obj = self._les_kategori_fil(kategorier + ".txt")
            self._meny[kat] = kat_obj
    
    def hentRedusertMeny(self, innholdsliste):
        ny_ordbok = {}
        for kat in self._meny:
            retter = self._meny[kat].hentOKRetter(self, innholdsliste)
            if len(retter) > 0:
                ny_ordbok[kat] = self._meny[kat]
        return ny_ordbok
    
class Kunde():
    def __init__(self, telefonnummer, innholdsstoffer): #streng, liste
        self._telefonnummer = telefonnummer
        self._innholdsstoffer = innholdsstoffer

    def velgRetter(self, meny):
        bestillinger = []
        kategori_ordbok = meny.hentRedusertMeny(self._innholdsstoffer)
        for kategorinavn in kategori_ordbok:
            kategori_ordbok[kategorinavn].skrivUtRetter()
            svar = input("Velg rett: ")
            if svar != "":
                bestillinger.append(svar)
        return bestillinger
    
class TakeAway():
    def __init__(self, kategorier, kunde_fil):
        self._meny = Meny(kategorier)
        self._kundekatalog = self.lesKundefil(kunde_fil)

    def betjenKunde(self, telefonnummer):
        kunde = self._kundekatalog[telefonnummer]
        self.lagOgLeverMat(kunde.velg_retter(self._meny))
        

    def lagOgLeverMat(self, bestillinger):
        print("Bestillt: ")
        i = 1
        for rett in bestillinger:
            print(f"{i}. {rett}")
            i += 1

    def lesKundeFil(self, fil):
        pass

def hovedprogram():
    kategorier = ["Forreter", "Hovedretter", "Desserter"]
    takeaway = TakeAway(kategorier, "Kunder.txt")
    telefonnummer = input("Skriv inn tlfnmr: ")
    while telefonnummer != "":
        takeaway.betjenKunde(telefonnummer)
        telefonnummer = input("Skriv inn tlfnmr: ")
    
    print("Programmet Avsluttes")