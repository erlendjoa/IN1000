#Oppgave 3.

#1. Først har jeg laget en tom liste steder, og med en for-løkke i en range av 5 ber bruker fylle inn reisemål i denne lista.

steder = []

for element1 in range(0,5):
    element1 = input("Skriv inn reisemål: ")
    steder.append(element1)

#2. To nye lister som fungerer på samme måte som i oppgave 1.

klesplagg = []
avreisedato = []

v1 = 0
for element2 in range(0,5):
    element2 = input(f"Skriv inn avreisedato til {steder[v1]}: ")
    avreisedato.append(element2)
    v1 += 1

v2 = 0
for element3 in range(0,5):
    element3 = input(f"Skriv inn klesplagg for reisen til {steder[v2]}: ")
    klesplagg.append(element3)
    v2 += 1

#3. Her definerer jeg variabelen reiseplan til en liste bestående av de tre listene over. 
#4. Deretter skriver jeg dem ut hver for seg med en for-løkke, som går gjennom hvert element i lista og skriver det ut.

reiseplan = [steder]+[avreisedato]+[klesplagg]
for element in reiseplan:
    print(element)

#5. Med en for loop for lengden på reiseplanen vil bruker få skrive inn hvilken reiseplan den kan velge å skrive ut.
# Med en If sjekker jeg om tallverdien er innenfor rekkevidde av liste, om den ikk er det vil en egen print bli printet ut.
# Om den er en verdi i reiseplan (-1) vil en ny input spørre om hvilket element i den gitte reiseplanen. Samme her,
# vil enten valgt input bli printet ut eller en egen tekst ("Ugyldig input!").

lengde = len(reiseplan)
for lengde in reiseplan:
    inp1 = int(input("Skriv hvilken reiseplan: "))-1
    if inp1 >=0 and inp1 <3:
        index2 = reiseplan[inp1]
        inp2 = int(input(f"Skriv hvilket element av {reiseplan[inp1]} du vil ha: " ))-1
        if inp2 >=0 and inp2 <5:
            print(reiseplan[inp1][inp2])
        else:
            print("Ugyldig input!")
    else:
        print("Ugyldig input!")