#Oppgave 3.

#Først defineres prosedyren minFunksjon() uten noen parametere. Så defineres prosedyren hovedprogram(). Så kjøres hovedprogram().
# variabelen a og b defineres til 42 og 0, så skrives ut til terminalen. Dermed får variabelen b en ny verdi lik a, altså 42.
# Så får på samme måte variabelen a en ny verdi, denne gangen for prosedyren minFunksjon(). Til slutt i hovedprogram() printes ut
# variabel b (42) og så printes ut a, som nå har verdien minFunksjon(), så denne prosedyren kjøres.
# minFunksjon() starter med en for loop, som vi ser kommer til å kjøres to ganger (range(2)). c defineres til 2 og printes ut. 
# c blir gjort om til 3 med en +=. Etter dette vil vi møte på problemet med denne koden. Programmet prøver å addere b med a via en +=.
# Ettersom a ikke er definert i minFunksjon() vil ikke python kjenne igjen variablene a. Variabelen er ikke definert i funksjonen.