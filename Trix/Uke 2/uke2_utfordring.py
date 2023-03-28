
def Ruritania():
    inp = input("Tast inn din inntekt:\n> ")
    inntekt = float(inp)

    if inntekt < 10000:
        skatt = inntekt*0.1
    else: 
        skatt = inntekt*0.3 + (inntekt - 10000)*0.3
    print("Skatt: ", skatt)
#Ruritania():


def kalkulator():
    tall1 = float(input("Første tall: "))
    operasjon = input("Operasjon: ")
    tall2 = float(input("Andre tall: "))

    if operasjon == "+":
        print(tall1, "+", tall2, "=", tall1 + tall2)
    elif operasjon == "-":
        print(tall1, "-", tall2, "=", tall1-tall2)
    elif operasjon == "/":
        print(tall1, "/", tall2, "=", tall1/tall2)
    elif operasjon == "*":
        print(tall1, "*", tall2, "=", tall1*tall2)
    else: 
        print("Det forstod jeg ikke")
#kalkulator()

def ifibutikk():
    inp = input(("Skriv inn din saldo: "))
    saldo = int(inp) 

    brød = 20
    melk = 15
    ost = 40
    yoghurt = 12

    handle = input("Hva vil du handle? (brød, melk, ost, yoghurt): ")
    if handle=="brød" and saldo>=brød:
        saldo = saldo-brød
        print("Her har du et brød. Du har nå ", saldo, "kroner igjen på din saldo.")
    elif handle=="melk" and saldo>=melk:
        saldo = saldo-melk
        print("Her har du melk. Du har nå ", saldo, "kroner igjen på din saldo.")
    elif handle=="ost" and saldo>=ost:
        saldo = saldo-ost
        print("Her har du en ost. Du har nå ", saldo, "kroner igjen på din saldo.")
    elif handle=="yoghurt" and saldo>=yoghurt:
        saldo = saldo-yoghurt
        print("Her har du en yoghurt. Du har nå ", saldo, "kroner igjen på din saldo.")
    elif handle=="brød" or "melk" or "ost" or "yoghurt" and saldo<brød or melk or ost or yoghurt:
        print("Du har ikke nok kroner på din saldo for dette kjøpet.")
    else: 
        print("Det har vi ikke i butikken.")
ifibutikk()