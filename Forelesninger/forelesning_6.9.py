#Lister:
variabel = [1, 2, 3, 4]
variabel = [2]*4
print(variabel)

variabel[1] = 5
print(variabel)


hoydeAar = []
hoydeAar.append(50) 
print(hoydeAar)

#liste = []
#liste.append
#liste.count("")
#len(liste)

muligheter = []
terning = int(input("Skriv inn et terningkast: "))
muligheter.append(terning)
print(muligheter)


#Menger:
min_mengde = {1, 2, 3, 4}
2 in min_mengde

yatzy = False
kast = []
kast.append(int(input("Kast: ")))
kast.append(int(input("Kast: ")))
kast.append(int(input("Kast: ")))
kast.append(int(input("Kast: ")))
kast.append(int(input("Kast: ")))

mengde = set(kast)

if len(mengde)==1:
    yatzy = True
    print("Yatzy!")
elif len(mengde)==2 and mengde.count(mengde[0] in [2, 3]):
    print("hus")
else:
    print("ikke yatzy..")

#Ordbøker/Dictionaries
hoydeAar = [1, 2, 3, 4]
by = {"Norge":"Oslo", "Tyskland":"Berlin", "Italia":"Roma"}
print(by["Italia"])

person = input("Konge: ")
etterkommere = {"Oscar":"Haakon", "Haakon":"Olav"}
barn = etterkommere(person)
barnebarn = etterkommere(barn)
print(barn, barnebarn)
#Over funker ikke?

#Nøstede samlinger
frokoster = [["egg", "bacon"], ["ost", "agurk"]]
assert frokoster[0][1]=="bacon"

if [0][1]+[0][0] == [1][0]+[1][1]:
    alle_like = True