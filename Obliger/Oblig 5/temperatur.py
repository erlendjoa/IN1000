#Oppgave 4.

def main():

#1. Her har jeg laget en tom ordbok, forså gjennom funksjonen å bruke en for-loop som går gjennom hver kodelinje i filen,
# og splitter linjen med en split(","). Så definerer jeg variabelen nøkkel til å være det første elementet i lista "linje",
# forså å legge det til i ordboka med "innhold" som innholdsverdi (float(linje[1], altså det andre elementet i lista "linje".))

    ordbok1 = {}

    def func1(x):
        csv1 = open(x, "r")
        for e in csv1:
            linje = e.strip().split(",")
            nøkkel = linje[0]
            innhold = float(linje[1])
            ordbok1[nøkkel] = innhold
        return ordbok1
        
    print(func1("Obliger\Oblig 5\max_temperatures_per_month.csv"))

#2/3. Her har jeg laget en funksjon som tar inn fil og ordbok fra oppgave 1, og oppdaterer ordboken med de nye høyeste varmetemperaturene.

    def func2(x, y):
        alleDager = open(x, "r")
        listeHoved = []
        listeMaaneder = []
        for e in alleDager:
            linje2 = e.strip().split(",")
            listeHoved.append(linje2)
        for e in y:
            listeMaaneder.append(e)

        hJan = y.get("Jan")             #Med .get definerer jeg varmeste temperaturen for hver måned i egne variabler
        hFeb = y.get("Feb")
        hMar = y.get("Mar")
        hApr = y.get("Apr")
        hMay = y.get("May")
        hJun = y.get("Jun")
        hJul = y.get("Jul")
        hAug = y.get("Aug")
        hSep = y.get("Sep")
        hOct = y.get("Oct")
        hNov = y.get("Nov")
        hDec = y.get("Dec")
        dJan = 0                #dag definert som 0
        dFeb = 0
        dMar = 0
        dApr = 0
        dMay = 0
        dJun = 0
        dJul = 0
        dAug = 0
        dSep = 0
        dOct = 0
        dNov = 0
        dDec = 0

        i = 0
        for e in listeHoved:            #for løkke som skjekker hvert element i lista og om de er over en måneds varmeste temp og
                                        #gjør dem om til varmeste temp i ordboka

            if (float(e[2]) > float(hJan)) and e[0] == "Jan":
                hJan = e[2]
                dJan = e[1]
                y["Jan"] = float(e[2])
            if (float(e[2]) > float(hFeb)) and e[0] == "Feb":
                hFeb = e[2]
                dFeb = e[1]
                y["Feb"] = float(e[2])
            if (float(e[2]) > float(hMar)) and e[0] == "Mar":
                hMar = e[2]
                dMar = e[1]
                y["Mar"] = float(e[2])
            if (float(e[2]) > float(hApr)) and e[0] == "Apr":
                hApr = e[2]
                dApr = e[1]
                y["Apr"] = float(e[2])
            if (float(e[2]) > float(hMay)) and e[0] == "May":
                hMay = e[2]
                dMay = e[1]
                y["May"] = float(e[2])
            if (float(e[2]) > float(hJun)) and e[0] == "Jun":
                hJun = e[2]
                dJun = e[1]
                y["Jun"] = float(e[2])
            if (float(e[2]) > float(hJul)) and e[0] == "Jul":
                hJul = e[2]
                dJul = e[1]
                y["Jul"] = float(e[2])
            if (float(e[2]) > float(hAug)) and e[0] == "Aug":
                hAug = e[2]
                dAug = e[1]
                y["Aug"] = float(e[2])
            if (float(e[2]) > float(hSep)) and e[0] == "Sep":
                hSep = e[2]
                dSep = e[1]
                y["Sep"] = float(e[2])
            if (float(e[2]) > float(hOct)) and e[0] == "Oct":
                hOct = e[2]
                dOct = e[1]
                y["Oct"] = float(e[2])
            if (float(e[2]) > float(hNov)) and e[0] == "Nov":
                hNov = e[2]
                dNov = e[1]
                y["Nov"] = float(e[2])
            if (float(e[2]) > float(hDec)) and e[0] == "Dec":
                hDec = e[2]
                dDec = e[1]
                y["Dec"] = float(e[2])

            if i != 11:
                i +=1
        
        '''
        if float(hJan) > y.get("Jan"):          #If-sjekk om det har blitt en ny varmerekord for hver måned
            print(f"Ny varmerekord for {dJan}. jan: {hJan}.")
        if float(hFeb) > y.get("Feb"):
            print(f"Ny varmerekord for {dFeb}. feb: {hFeb}.")
        if float(hMar) > y.get("Mar"):
            print(f"Ny varmerekord for {dMar}. mar: {hMar}.")
        if float(hApr) > y.get("Apr"):
            print(f"Ny varmerekord for {dApr}. apr: {hApr}.")
        if float(hMay) > y.get("May"):
            print(f"Ny varmerekord for {dMay}. mai: {hMay}.")
        if float(hJun) > y.get("Jun"):
            print(f"Ny varmerekord for {dJun}. jun: {hJun}.")
        if float(hJul) > y.get("Jul"):
            print(f"Ny varmerekord for {dJul}. jul: {hJul}.")
        if float(hAug) > y.get("Aug"):
            print(f"Ny varmerekord for {dAug}. aug: {hAug}.")
        if float(hSep) > y.get("Sep"):
            print(f"Ny varmerekord for {dSep}. sep: {hSep}.")
        if float(hOct) > y.get("Oct"):
            print(f"Ny varmerekord for {dOct}. oct: {hOct}.")
        if float(hNov) > y.get("Nov"):
            print(f"Ny varmerekord for {dNov}. nov: {hNov}.")
        if float(hDec) > y.get("Dec"):
            print(f"Ny varmerekord for {dDec}. dec: {hDec}.")
        '''
        return y
        
    
    print(func2("Obliger\Oblig 5\max_daily_temperature_2018.csv", ordbok1))

main()