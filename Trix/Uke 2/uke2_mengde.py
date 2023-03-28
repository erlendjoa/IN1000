#02.06:

#her sliter jeg med å lage int variabel inne i def.
"""
def prosedyre():
    x = input(int("skriv et heltall: "))
    y = input(int("skriv et til heltall: "))
    differanse = x - y
    print(str(differanse))

prosedyre()

def differanse():
    inp = input("Oppgi verdien til x:\n> ")
    x = int(inp)

    inp = input("Oppgi verdien til y:\n> ")
    y = int(inp)

    print(x - y)

differanse()
"""
#02.08:
def kroppstemp():
    inp = input("skriv inn din kroppstemperatur: ")
    temp = float(inp)

    if temp >= 36.5 and temp <= 37.5:
        print("normal kroppstemperatur.")
    elif temp < 36.5:
        print("lav kroppstemperatur.")
    else: print("høy kroppstemp")

kroppstemp()