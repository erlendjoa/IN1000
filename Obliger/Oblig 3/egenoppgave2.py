#Lag en gjesteliste med ordbøker og lister. Få til at programmet spør som hvor mange gjester som skal delta, forså å svare med hvilke 
# allergener gjestene har. Bruk både if-setninger, ordbøker, prosedyrer og lister i programmet.

ordbok = {}
gjester = []

def allergenpros():
    if antall==1:
        ordbok[gjester[0]] = input("Skriv inn allergener til " + gjester[0] + ": ")
    elif antall==2:
        ordbok[gjester[0]] = input("Skriv inn allergener til " + gjester[0] + ": ")
        ordbok[gjester[1]] = input("Skriv inn allergener til " + gjester[1] + ": ")
    elif antall==3:
        ordbok[gjester[0]] = input("Skriv inn allergener til " + gjester[0] + ": ")
        ordbok[gjester[1]] = input("Skriv inn allergener til " + gjester[1] + ": ")
        ordbok[gjester[2]] = input("Skriv inn allergener til " + gjester[2] + ": ")

def gjestepros():
    gjester.append(input("Skriv inn navn på en gjest: "))
    spør = input("Er det flere gjester? (ja/nei): ")
    if spør=="ja":
        gjestepros()

print("Velkommen til event påmelding!")
gjestepros()

print("Antall gjester er satt til "+ str(len(gjester)) + " stk: " + str(gjester))
antall = len(gjester)

allergenpros()

if antall<4:
    print("Antall gjester og hvilke allergener som bør styres unna er følgende: "+ str(ordbok))
else:
    allergen = input("Siden antall gjester er " + str(antall) + " vil ikke kokken ha kapasitet til å lage spesielle retter til hver enkelt person. Skriv inn allergen som bør styres unna (blir laget til alle pers): ")
    print("Deltakere som skal delta er: " + str(gjester) + ". Allergener som bør styres unna er: " + allergen)

if antall==1:
    print("Takk for info, gleder oss til å se deg:)")
else:
    print("Takk for info, gleder oss til å se dere:)")


    




