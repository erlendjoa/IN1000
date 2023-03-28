from random import randint

tema = []

def filaapner(fil):
    for i in fil:
        lin = i.strip().split(":")
        tema.append(lin)

def hent_tilfeldig_tema():
    int = randint(0,len(tema)-1)
    return [tema[int][0], tema[int][1]]

def quizpros():
    tilfeldigTema = hent_tilfeldig_tema()
    print("*****************************************")
    print(tilfeldigTema[0])
    input("")
    print(tilfeldigTema[1])
    quizpros()

filaapner(open("privat/1050quiz/alleTemaer.csv"))
quizpros()