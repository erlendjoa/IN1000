#Oppgave 1.

#1. Her har jeg skrevet en funksjon med to parametere som adderes sammen til en variabel (x)

def func1(x, y):
    x += y
    return x
    
print(func1(2,6))

#2. Her definerer jeg to nye funksjoner med subtraksjon og divisjon. Etter noen prints skjekker jeg med assert om gitte
# verdier er lik (==) en sum. 

def func2(x, y):
    y -= x
    return y

def func3(x, y):
    x /= y
    return x

print(func2(2,6))
print(func2(-5,-3))
print(func3(5,15))
'''
assert func1(2, 7) == 9          #Her har jeg valgt å commente ut assert, ettersom oppgave 4/5 bruker funksjonene.
assert func2(-5, -3) == 2
assert func3(-1,8) == -0.125
'''

#3. Funksjonen her skjekker med assert om tall kalt med funkjsonen er større enn null, og deretter returnerer
# tallet etter en multiplikasjon med 2.54.

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer*2.54
print(tommerTilCm(5))

#4/5. Prosedyren her tar for seg 3 input linjer, hvor 2 av dem blir brukt i de 3 funksjonene i oppgavene over. Resultat blir
# printet ut. Deretter blir den siste input verdien kalt inn i funksjonen "tommerTilCm", og resultat blir printet ut.

def skrivBeregninger():
    inp1 = input("Skriv inn tall for verdi x: ")
    inp2 = input("Skriv inn tall for verdi y: ")
    verdix = float(inp1)
    verdiy = float(inp2)
    print(f"Resultat av addisjon: {func1(verdix, verdiy)}")
    print(f"Resultat av subtraksjon: {func2(verdix, verdiy)}")
    print(f"Resultat av divisjon: {func3(verdix, verdiy)}")
    inp3 = input("Skriv inn tall i tommer: ")
    verdit = int(inp3)
    print(f"Resiltat av {verdit} tommer til Cm er: {tommerTilCm(verdit)}")
skrivBeregninger()