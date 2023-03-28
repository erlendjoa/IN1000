
#Programmet ber om en input i Fahrenheit, forså å gjøre om svaret til datatypen float, og deretter string igjen under print kommandoene.

inp = input("Skriv inn temperatur i Fahrenheit: ")
fahr = float(inp)
print("Temperatur i fahrenheit er " + str(fahr))

celsius = (fahr - 32)*5/9
print("Temperatur i celsius er " + str(celsius))