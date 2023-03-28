#Oppgavetekst: Lag en quiz med If/else kommandoer og et poengsystem med minus/pluss-poeng. Før quizen begynner skal programmet spørre om navnet til brukeren og om de er klare
# til å begynne quizen. Quizen skal ikke begynne før brukeren er klar. Lag 3 spørsmål brukeren skal svare på. 

def velkommen():
    navn = input("Velkommen til Quiz! Skriv ditt navn: ")
    print("Hei " + navn + ". Du skal nå svare på 3 spørsmål. Det blir gitt poeng for riktig svar, og minuspoeng for feil svar.")
    klar = input("Er du klar? (ja/nei): ")
    if klar=="ja":
        print("Her kommer første spørsmål.")
    else:
        velkommen()
velkommen()

poeng=0

svar1 = input("Hvor mange dager er det i februar måned i et skuddår?: ")
if svar1!="29":
    poeng = poeng-5
    print("Feil svar! Svaret var 29. Du har nå " + str(poeng) + " poeng.")
else:
    poeng = poeng+10 
    print("Riktig svar! Dine poeng: " + str(poeng))


svar2 = input("Hvilket kontinent ligger Australia i?: ")
if svar2!="Oseania":
    poeng = poeng-5
    print("Feil svar! Svaret var Oseania. Du har nå " + str(poeng) + " poeng.")
else:
    poeng = poeng+10
    print("Riktig svar!")


svar3 = input("Hvor mange stjerner er det i det amerikanskje flagget?: ")
if svar3!="50":
    poeng = poeng-5
    print("Feil svar! Svaret var 29. Du har nå " + str(poeng) + " poeng.")
else:
    poeng = poeng+10
    print("Riktig svar!")


if poeng>=30:
    print("Quizen er ferdig. Du har alt riktig, og nådde en score på " + str(poeng) + " poeng!")
else:
    print("Quizen er ferdig. Du nådde en score på " + str(poeng) + " av 30 poeng.")