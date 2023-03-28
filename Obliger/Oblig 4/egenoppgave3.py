#5. Egenoppgave

#Oppgavetekst: Lag et program for å holde styr på bursdagen til vennene dine. Programmet må bestå av en liste, funksjon og en loop
# med input verdier. Til slutt skal det printes ut en oversikt over dine venner og deres bursdager.

ordbok = {}
venneliste = []

def nr1(x):
    for elem1 in range(x):
        venneliste.append(input("Skriv inn navn på venn: "))

inp1 = input("Hvor mange venner skal du skrive ned bursdagen til?: ")
antall_venner = int(inp1)
nr1(antall_venner)

for elem2 in venneliste:
    bursdag_måned = input(f"Nummer på måneden {elem2} har bursdag: ")
    bursdag_dag = input(f"Dag i måned nr {bursdag_måned}: ")
    bursdag = (f"{bursdag_dag}.{bursdag_måned}")
    ordbok[elem2] = bursdag
print(f"Her er en oversikt over dine venner og deres bursdager: {ordbok}")

