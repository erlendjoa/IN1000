#1. Her har jeg laget en liste med navn "liste". Den består av 3 elementer, men jeg bruker append for å legge
# til et ekstra tall. Dermed skriver jeg ut kun det første og tredje tallet i lista. 
liste = [2, 4, 8]
liste.append(16)

print(liste[0],liste[2])

#2. Her er en ny tom liste. Jeg bruker append og dermed en input hvor brukeren kan legge til noe i lista.
ny_liste = []
ny_liste.append(input("Oppgi et navn: "))
ny_liste.append(input("Oppgi et navn: "))
ny_liste.append(input("Oppgi et navn: "))
ny_liste.append(input("Oppgi et navn: "))

#3. If, Else er her med en "not in", for å se om navnet mitt er lagt til i lista. Om den ikke er lagt til, vil en egen print skrives ut.
if "Erlend" not in ny_liste:
    print("Glemte du meg?")
else:
    print("Du husket meg!")

#4. Her lager jeg først en tom liste, og bruker append for å legge til summen og multiplikasjonen av tallene i lista fra oppgave 1.
# deretter fjerner jeg de 2 siste tallene fra lista med "pop", og printer ut. 
listeplus = []
listeplus.append(liste[0] + liste[1] + liste[2] + liste[3])
listeplus.append(liste[0]*liste[1]*liste[2]*liste[3])
listemulti = liste + listeplus
print(listemulti)

listemulti.pop(5)
listemulti.pop(4)
print(listemulti)