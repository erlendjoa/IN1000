#1. Her har jeg laget en ordbok med {}. Jeg bruker varenavn som nøkkelverdier og varepriser som innholdsverdier med :
varer = {"melk":14.90 , "brød":24.90 , "yoghurt":12.90 , "pizza":39.90}
print(varer)

#2. Her ber jeg bruker skrive inn en ny vare og pris til vare, forså å legge dem til i ordboken.

vare1 = input("Skriv inn nøkkelverdi: ") 
pris1 = input("Skriv inn innholdsverdi; ")
vare2 = input("Skriv inn nøkkelverdi: ") 
pris2 = input("Skriv inn innholdsverdi; ")

varer[vare1] = pris1
varer[vare2] = pris2
print(varer)