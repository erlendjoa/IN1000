#Oppgave 1.
#Nr 1: Denne filen har navn "variabler.py"

#Nr 2: Her skriver jeg ut en enkel print kommand til terminalen:
print("Hei Student!")

#Nr 3: Her ber jeg brukeren oppgi sitt navn, deretter hilser på brukerens oppgitte navn. 
navn_1 = input("Oppgi ditt navn: ")
print("Hei", navn_1) 

#Nr 4: Her har jeg laget to variabler, deretter printet dem ut på hver sin linje.
nummer_1 = 6
nummer_2 = 4
print(nummer_1)
print(nummer_2)

#Nr 5: Her har jeg definert en ny variabel som printer ut differansen mellom de to variablene i nr 4.
Differanse = nummer_1 - nummer_2
print(Differanse)

#Nr 6: Her ber jeg bruker skrive inn et nytt navn, som blir lagret i en ny variabel. Deretter printes ut de to varablene som
# inneholder navnene ut på samme linje via en ny variabel (sammen).
navn_2 = input("Oppgi et nytt navn: ")
sammen = navn_1 + navn_2
print(sammen)

#Nr 7: Her har jeg endret variabelen "sammen" ved å bruke en ny linje til å definere variabelen med et " og " print imellom variablene.
sammen = navn_1 + " og " + navn_2
print(sammen)
