maaned = ["jan", "feb", "mar", "apr", "mai", "jun", "jul", "aug", "sep", "okt", "nov", "des"]
inp = input("skriv inn månedsnummer: ")
nr = int(inp)


if nr > 0 and nr < 13 :
    print(nr, "-", maaned[nr-1])
else:
    print("Ugyldig maanedsnr")