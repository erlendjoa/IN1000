#Oppgave 3: Her har jeg laget et program som ber bruker skrive inn to datoer. Deretter skjekker programmet om verdien av den
# ene datoen er høyere, lavere eller lik som den andre. I terminalen printes dette ut i text.
""""
a = input("Skriv inn en dato: ")
b = input("Skriv inn en annen dato: ")

if a < b:
    print("Riktig rekkefølge!")
elif a==b:
    print("Samme rekkefølge!")
else: print("Feil rekkefølge!")

"""

a = input("skriv inn en dato nr. 1: ")
b = input("skriv inn måned nr. 1: ")
c = input("skriv inn dato nr. 2: ")
d = input("skriv inn måned nr. 2: ")

dato1 = int(a and b)
dato2 = int(c and d)

if b < d:
    print("riktig rekkefølge.")
elif b==d and a==c:
    print("samme rekkefølge.")
elif b==d and a < c:
    print ("riktig rekkefølge.")
else: print("feil rekkefølge.")