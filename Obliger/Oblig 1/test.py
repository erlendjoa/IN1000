

svar_1 = "Her har du en brus!"
svar_2 = "Den er grei."
svar_3 = "Det forstod jeg ikke helt."

svar_1 = False
svar_2 = False
svar_3 = False

brus = input("Kunne du tenke deg en brus? (ja/nei): ")
if brus=="ja":
    svar_1 = True
if brus=="nei":
    svar_2 = True
else: svar_3 = True

if svar_1==True:
    print("Her har du en brus!")
if svar_2==True:
    print("Den er grei.")
if svar_3==True:
    print("Det forstod jeg ikke helt.")