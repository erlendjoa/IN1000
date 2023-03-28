from hund import Hund

def hovedprogram():      #6. Hunden doggo blir definert som Hund, og den bruker spring() og spis() som øker og reduserer vekt.
    doggo = Hund(8,6)
    print(doggo.vekt)
    print(doggo.alder)
    doggo.spring()
    print(doggo.vekt)
    doggo.spring()
    print(doggo.vekt)
    doggo.spis(3)
    print(doggo.vekt)
    doggo.spis(2)
    print(doggo.vekt)

hovedprogram()