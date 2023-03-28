#print kommando
from encodings import normalize_encoding


print("hei IN1000")
print(3+2)

#variabler:
tall = 13
print(tall)

#videre om variabler:
lengde = 5
bredde = 4
areal = lengde*bredde
print(areal)

pris = 5
print("to epler koster: ")
print(pris*2)

#input:
navn = input("Skriv ditt navn: ")
print("hei", navn)

#beslutninger:
land = input("velg land i nordre skandinavia: ")
if land =="Norge":
    print("Oslo")
if land =="Sverige":
    print("Stockholm")
else: print("Dette er ikke et land i nordre skandinavia")


alder = input("Er du voksen? (ja/nei): ")
if alder=="ja":
    input("Er du gravid? (ja/nei): ")
    if input=="ja":
        print("Du er en voksen gravid")
    else: print("Du er ikke gravid men voksen")
else: print("Du er ikke voksen")