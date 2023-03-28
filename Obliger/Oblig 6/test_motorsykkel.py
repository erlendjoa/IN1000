from motorsykkel import Motorsykkel    #4. Importerer classen motorsykkel og laget et hovedprogram().

def hovedprogram():         #5. Her oppretter jeg 3 objekter av typen Motorsykkel

    ferrari = Motorsykkel("458 Italia", "BR1234567890")  #6. Her skriver jeg ut metodene skriv_ut() på alle objektene
    volkswagen = Motorsykkel("Golf", "BP0987654321")
    honda = Motorsykkel("G5", "BR1029384756")
    ferrari.skriv_ut()
    volkswagen.skriv_ut()
    honda.skriv_ut()

    honda.kjor(10)        #7. Her bruker jeg først metoden kjor() for å øke total km avstand til honda.
    print(honda.hent_kilometerstand())      #Så printer jeg det som blir returnet, som er det totale + avstanden til honda.
hovedprogram()