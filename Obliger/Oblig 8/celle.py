class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
        self._lever = False

    def sett_doed(self):
        self._status = "doed"
        self._lever = False

    def sett_levende(self):
        self._status = "levende"
        self._lever = True

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def er_levende(self):
        return self._lever

    def hent_status(self):
        return self._status

    def hent_status_tegn(self):
        if self._lever == True:
            return "O"
        else:
            return "."

    def tell_levende_naboer(self):
        self._ant_levende_naboer = 0
        for e in self._naboer:              #går gjennom naboer og for hver levende legger til 1 i ant_lev_naboer
            if e.er_levende() == True:
                self._ant_levende_naboer += 1

    def oppdater_status(self):
        if self.er_levende() == True:               #sjekker cellen først om den er levende, om deretter hvor mange naboer.
            if self._ant_levende_naboer < 2:      #settes død om enkelte utsagn om antall naboer stemmer eller ikke
                self.sett_doed()
            elif self._ant_levende_naboer > 3:
                self.sett_doed()
        else:
            if self._ant_levende_naboer == 3:
                self.sett_levende()
