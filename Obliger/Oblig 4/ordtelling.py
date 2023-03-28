#Oppgave 4.

#1. Funkjsonen her ber om et ord i input og returnerer lengden av dette ordet.

ord = input("Skriv et ord: ")
def func(x):
    antall = len(ord)
    return antall
bokstaver = func(ord)
print(f"Ordet '{ord}' har {bokstaver} bokstaver i seg.")


#2. Her lager jeg en tom ordbok. Input fra bruker blir gjort om til en liste med hvert ord for hvert element via
# .split(). Med en for-loop vil i en for-loop vil hvert ord i lista skjekkes opp mot hvert ord. Om det andre skjekkede ordet erlik 
# det første, vil variabelen "antall" øke med 1, til den andre for-loopen avsluttes. Etter det i samme første for-loop vil 
# "antall" legges til i ordboken som innholdsverdi for element1, altså ordet som skjekkes i den første loopen.

ordbok1 = {}
setning1 = input("Skriv inn en setning: ")   
liste1 = setning1.split() 

for element1 in liste1:
    antall = 0
    for element2 in liste1:
        if element2 == element1:
            antall +=1
    ordbok1[element1] = antall
print(ordbok1)


#3. I denne oppgaven er jeg klar over at print-funksjone i slutten av programmet ikke er hundre prosent feilfri, men jeg mener å ha fått med meg essensen
# i hva oppgaven spør om. Ønsker gjerne tilbakemelding på hvordan jeg kunne gjort det her.

# Her gjør jeg samme som i oppgave 2, bare at jeg tar med funksjonen laget i oppgave 1.
# Forskjellen her, er at i den andre for-loopen definerer jeg variablene "setninger" som en tekststreng, og en
# variabel "indeks" som element i ordboken på plassen "indeks_nummer" (en variabel med verdi 0 og øker med 1 for hver skjekk i for-loopen).
# Med en if-statement skjekker jeg om elementet i den første for-loopen ikke er i lista, så om den ER det, vil funksjonen func2 kjøres
# med ordet i for-loopen. Deretter vil en print skrives ut som kompinerer de to oppgavene.

ordbok2 = {}
setning2 = input("Skriv inn en setning: ")
liste2 = setning2.split()
lengde = len(liste2)


def func2(x):
    antall = len(x)
    return antall
ord2 = func2(liste2)
print(f"Setningen '{liste2}' har {ord2} ord i seg.")

indeks_nummer = 0
for element3 in liste2:
    antall = 0
    for element4 in liste2:
        if element4 == element3:
            antall +=1
    ordbok2[element3] = antall

    setninger = " "
    indeks = list(ordbok2)[indeks_nummer]

for word in ordbok2:
    ord3 = func2(word)
    print(f"Ordet {word} forekommer {ordbok2[word]} ganger, og har {ord3} bokstaver i seg.")