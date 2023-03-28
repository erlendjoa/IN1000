

#Oppgave 2.

# Her har jeg laget en tom liste forså å lage en variabel men en input med heltallsverdi. 
# Deretter har jeg en while-løkke som skjekker om variabelen "tall" ikke er null. Hvis tallet ikke er null, vil
# i løkken programmet legge til dette heltallet i lista. Etter bruker har tastet inn 0 vil løkken slutte, og programmet
# vil skrive ut alle tallene i lista med en for løkke. 

liste = []
tall = int(input("Skriv inn et tall: "))
liste.append(tall)

while tall != 0:
    tall = int(input("Skriv inn et tall: "))
    if tall != 0:
        liste.append(tall)
for tall in liste:
    print(tall)

#4. Her er en for løkke som summerer tallene sammen. For løkken går gjennom alle tallene i lista og legger 
# dem sammen i en egen variabel "minSum" som til slutt blir printet ut.

minSum = 0
for tall in liste:
    minSum += int(tall)
print(f"{minSum}")

#5. Her i programmet definerer jeg en variabel satt til det første elementet i lista. Deretter med en for-loop
# skjekker jeg hvert tall i lista om det er større enn verdien for "nummer". Om det skulle være tilfellet, vil 
# dette nye tallet som nå skjekkes i lista bli den nye verdien for "nummer". 

nummer = liste[0]
for tall in liste:
    if tall > nummer:
        nummer = tall
print(nummer)