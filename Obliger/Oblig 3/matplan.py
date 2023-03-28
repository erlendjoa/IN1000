#1. Her har jeg laget lister med matplan og deretter en ordbok hvor listene befinner seg i. Jeg vet det er mulig å lage listene inne i ordboken også
# men likte måten å gjøre det på sånn som jeg har gjort her. 
måltid = ["frokost", "bacon"]
måltid2 = ["lunsj", "eggerøre"]
måltid3 = ["middag", "pasta"]
sykehjem = {"Ola":måltid, "Kari":måltid2, "Jens":måltid3}

#2. Her har jeg laget en prosedyre som ber bruker skrive inn navn på beboer, for deretter å sende ut matplan.
def prosedyre():
    print(sykehjem)
    navn = input("Skriv inn navn på beboer: ")
    if navn in sykehjem:
        print(sykehjem[navn])
    else:
        print("Navn ikke funnet.")
prosedyre()

#3. 
# a) Jeg ville brukte en mengde for brukernavn på alle IN1000 elevene, ettersom den kun tar for seg ikke-duplikater.
# b) Jeg ville brukt en ordbok, hvor nøkkelverdi er brukernavn og innholdsverdi er poeng.
# c) Jeg ville brukt en ordbok om jeg skulle hatt med lottotallene til personene. Da ville jeg hatt navnene som nøkkelverdi og tallene som innholdsverdi
# om det kun er snakk om navn, vil en liste kunne la seg gjøre, ettersom den kan ha like navn. 
# d) Jeg ville brukt en ordbok med gjester som nøkkelverdi, og hvilke allergener det gjelder som innholdsverdi.