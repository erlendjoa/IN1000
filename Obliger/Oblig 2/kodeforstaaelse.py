#1. Ja, programmet vil kunne kjøre, men vil ikke funke slik vi vil. Programmet spør om et heltall som input,
# og gjør deretter denne textverdien om til en heltallsverdi, men prøver så å printe ut en heltallsverdi sammen med en string,
# noe som ikke går. Vi får dermed en feilmelding.
#2. Vi vil møte på en feilmeldig dersom tallet som input er under 10, ettersom
# to datatyper ikke kan printes ut samtidig (feks: str og int). 
# Vi kan også møte på forvirring om tallet vi velger som input ikke er under 10,
# ettersom koden ikke definerer en else verdi for heltall over eller erlik 10. Det vil ikke skrives ut noe om dette er tilfellet. 

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")

