#Oppgave 6. Oppgavetekst gitt i oblig 6 oppgavetekst. 

class Person:                                   #Her har jeg laget en klasse Person som tar inn navn, alder
        def __init__(self, navn, alder):
            self.navn = navn
            self.alder = alder
            self.hobbyer = []
            self.s = ""
        def leggTilHobby(self, tekststreng):    #Metode som legger til hobbyer i liste med hobbyer
            self.hobbyer.append(tekststreng)
        def skrivHobbyer(self):                 #Metode som først legger sammen alle elementer i hobbylista lager dem til 1 streng
            for e in self.hobbyer:              # forså å printe ut denne strengen.
                self.s += f"{e}, "
            print(self.s)
        def skrivUt(self):                      #Metode som skriver ut navn, alder og hobbyer til objektet.
            print(f"Navn: {self.navn}\nAlder: {self.alder}\nHobbyer: {self.hobbyer}")

def hovedprogram():
    navn = input("Skriv inn fullt navn: ")
    alder = int(input(f"Skriv inn alder på {navn}: "))
    p1 = Person(navn, alder)

    hobby = input(f'Skriv inn hobby til {navn} ("f" for å gå videre): ')
    while hobby != "f":
        p1.leggTilHobby(hobby)
        hobby = input(f'Skriv inn hobby til {navn} ("f" for å gå videre): ')
    p1.skrivHobbyer()
    p1.skrivUt()
hovedprogram()
