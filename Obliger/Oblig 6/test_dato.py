from dato import Dato

def hovedprogram():

    d1 = Dato(1, 5, 2021)     #2. Definering av første dato med dag 15 som parameter.
    print(d1.hent_aar())    #4a.

    if d1.sjekk_dato() == True: #4b.
        print("Loenningsdag!")
    elif d1.sjekk_dato == 1:                        #FUNGERER IKKE
        print("Ny maaned, nye muligheter")

    dato = d1.hent_alt()  #4c.
    print(dato)         #4d.
hovedprogram()