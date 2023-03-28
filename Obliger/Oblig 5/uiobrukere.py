#Oppgave 2.

#1. Funksjonen her tar inn en verdi for x, som jeg har satt til å være navnet. Med .split() vil det dannes en liste med de to
# ordene. Med det lager jeg en f string som returnerer det første ordet, og den første bokstaven i det andre ordet.

def lagBrukernavn(x):
    liste = x.split(" ")
    return f"{liste[0]}{liste[1][0]}"
navn = input("Skriv inn ditt fulle navn (fornavn og etternavn): ")
print(lagBrukernavn(navn))

#2. Funksjonen tar inn navn og suffix og kombinerer dette sammen med en @ imellom, og returnerer denne nye strengen.

def lagEpost(x, y):
    return f"{x}@{y}"


brukernavn = input("Skriv inn ditt fornavn: ")
suffix = input("Skriv inn suffix: ")
print(f"Din epost er satt til {lagEpost(brukernavn, suffix)}")

#3. Funksjonen her skjekker hvert element i ordboka med en for loop, og lager eposter via lagEpost() med nøkkelverdien og innholdsverdien
# som parametere.

def skrivUtEposter(x):
    for elem in x:
        print(lagEpost(elem, x[elem]))
ordbok = {"olan":"ifi.uio.no","karin":"student.matnat.no"}
skrivUtEposter(ordbok)

#4. Med oppgaveteksten ber programmet om inout i, p, eller s. Hver av bokstavene fører til et eget sett med kodelinjer via en 
# if-sjekk. Om bruker skriver inn "i", vil to inputer kjøre, og med funksjonen lagEpost, vil det lages en epost og legges til i
# den nye ordboka. Med "p" vil funksjonen skrivUtEposter kjøres med ordbok2 som parameter. Om brukeren ikke skriver noen av de tre
# bokstavene, vil "Ugyldig Input" skrives ut. For at while loopen skal gå om igjen vil inp1 kjøres i slutten av programmet.

ordbok2 = {}
inp1 = input("Skriv en av bokstavene (i, p, s): ")
while inp1 != "s":
    if inp1 == "i":
        brukernavn2 = input("Skriv inn ditt fornavn: ")
        suffix2 = input("Skriv inn suffix: ")
        epost = lagEpost(brukernavn2, suffix2)
        ordbok2[brukernavn2] = suffix2
    elif inp1 == "p":
        skrivUtEposter(ordbok2)
    else:
        print("Ugyldig input.")
    inp1 = input("Skriv en av bokstavene (i, p, s): ")

