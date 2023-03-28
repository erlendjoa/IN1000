#Her har jeg laget en prosedyre som ber om input og gjør om dette til en heltallsverdi.
# Deretter bestemmer if/else verdien til billettpris variabelen, og printer deretter ut hva prisen blir.

def prosedyre():
    inp = input("Skriv din alder: ")
    alder = int(inp)
    billettpris = 0
    if alder<18:
        billettpris = 30
        print("Billettprisen blir " + str(billettpris))
    elif alder>17 and alder<63:
        billettpris = 50
        print("Billettprisen blir " + str(billettpris))
    else:
        billettpris = 35
        print("Billettprisen blir " + str(billettpris))

prosedyre()