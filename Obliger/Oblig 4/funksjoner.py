

#Oppgave 1.

#1. Her har jeg laget en funksjon som tar inn verdier for "x" og "y", og returnerer summen av disse tallene.
# Dermed printer jeg to strenger med summen av de gitte tallene.

def adder(x,y):
    return x+y
print(f"Summen av tallene 2 og 5 blir {adder(2,5)}")
print(f"Summen av tallene 12 og 46 blir {adder(12,46)}")

#2/3 Her har jeg definert en funksjon som tar inn variabelen setning og bokstav, som bruker har definert via input. Funksjonen
# bruker en for loop som ser på hvert element i variabelen setning. Deretter for hver skjekk i for loopen, hvis bokstaven 
# definert av brukeren er den samme som elementet i setningen, vil variabelen "nummer" bli 1 større. Slik finner jeg ut
# av hvor mange det er av en gitt bokstav i en tekststreng. 

def pros(setning, bokstav):
    nummer = 0
    for elem in setning:
        if bokstav==elem:
            nummer += 1
    return nummer
    
setning = input("Skriv inn en setning: ")
bokstav = input("Velg bokstav: ")
print(f"Antall {bokstav}'er i setningen din er {pros(setning, bokstav)}.")
