class Lyspaere:
    def __init__(self):
        self._paa = False
    def er_paa(self):
        return self._paa
    def tenne(self):
        self.paa = True
    def slukke(self):
        self.paa = False
utelampe = Lyspaere()
status = utelampe.er_paa()
utelampe.tenne()