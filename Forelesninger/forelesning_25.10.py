class Node:
    def __init__(self, navn):
        self._navn = navn
        self._nabo = None
    
    def sett_nabo(self, nabo):
        self._nabo = nabo
    def hent_nabo(self):
        return self._nabo
    def hent_navn(self):
        return self._navn

    def hovedprogram(self, fil):
        forskningsparken = Node("Forskningsparken")
        forrige_stasjon = forskningsparken                  
        for e in open(fil,"r"):
            stasjon = Node(e.strip())               #.strip() for å slippe "\n" på slutten av tekststrenger
            forrige_stasjon.sett_nabo(stasjon)      #variabel blir satt til objektets _nabo.
            forrige_stasjon = stasjon
        
        maal = input("Hvor vil du reise?: ")
        her = forskningsparken
        while her.hent_navn() != maal:
            print(f"Du er her {her.hent_navn()}")
            her = her.hent_nabo()
        print(f"Du har ankommet {her.hent_navn()}")

liste = Node
liste.hovedprogram("hei","Forelesninger/fil.txt")
