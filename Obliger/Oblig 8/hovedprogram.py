from verden import Verden

def hovedprogram():
    rad = int(input("Antall rader: "))
    kol = int(input("Antall kolonner: "))
    verden = Verden(rad,kol)
    verden.oppdatering()

# starte hovedprogrammet
hovedprogram()