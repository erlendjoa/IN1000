from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def les_fil(self, filnavn):         #leser paramenter som fil, .strip().split() gjør fil om til liste og deler inn for hver ";".
        fil = open(filnavn, "r")
        for linje in fil:
            e = linje.strip().split(';')
            self._sanger.append(Sang(e[1],e[0]))    #oppretter et Sang objekt for hver liste i lista self._sanger, med indeks 0 og 1 (skilt med .split(";") over)

    def legg_til_sang(self, ny_sang):   #appender objektet ny_sang i self._sanger
        self._sanger.append(ny_sang)

    def fjern_sang(self, sang):         #for-løkke går gjennom lista, hvis objektet i parameter erlik objektet i lista bruker jeg .remove(parameter)
        for e in self._sanger:
            if sang == e:
                self._sanger.remove(e)

    def spill_sang(self, sang):         #bruker .spill() fra klassen Sang
        sang.spill()
    
    def spill_alle(self):       
        for e in self._sanger:
            e.spill()
    
    def finn_sang(self, tittel):        #for-løkke sjekker om tittel på sangene i lista erlik parameter. Isåfall, returner første funnet objekt med lik tittel.
        for e in self._sanger:
            if e.hent_tittel() == tittel:
                return e

    def hent_artist_utvalg(self, artistnavn):   #tom liste opprettes, og appender objekt hvis tekstrengen som parameter finnes i tekstrengen .hent_artist() fra Sang.
        liste = []
        for e in self._sanger:
            if artistnavn in e.hent_artist():
                liste.append(e)
        return liste