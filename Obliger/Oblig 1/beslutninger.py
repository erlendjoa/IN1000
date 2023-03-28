#Oppgave 2.
#Nr 1 og 2: Her lagrer jeg først verdier for to svar i to variabler (svar:1 og svar_2). Deretter definerer brukeren enten svaret 
# ja, nei, eller noe annet, hvor jeg deretter bruker if, elif, og else for å gi riktig output (svar_1, svar_2, eller en egen print).

svar_1 = "Her har du en brus!"
svar_2 = "Den er grei."

brus = input("Kunne du tenke deg en brus? (ja/nei): ")
if brus=="ja":
    print(svar_1)
elif brus=="nei":
    print(svar_2)
else: print("Det forstod jeg ikke helt.")
