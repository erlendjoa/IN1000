
#Her definerer vi prosedyren og spør om brukerens navn med en input kommando.
#Deretter skriver jeg ut prosedyren 3 ganger etterhverandre

def prosedyre():
    navn = input("Skriv inn ditt navn: ")
    bosted = input("Hvor kommer du fra: ")
    print("Hei " + navn + ". Du er fra " + bosted)

prosedyre()
prosedyre()
prosedyre()