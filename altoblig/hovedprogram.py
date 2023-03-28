import pgzrun
from spillbrett import Spillbrett
from random import randint

# Her lager vi et nytt spillbrett og oppretter to sauer med ulike bilder og ulike start-posisjoner
spillbrett = Spillbrett()
listeSauer = spillbrett.hent_sauer()
listeSteiner = spillbrett.hent_steiner()
listeGress = spillbrett.hent_gress()
spillbrett.opprett_sau("navn1", "sau",  randint(0,850), randint(0,650), listeGress)
spillbrett.opprett_sau("navn2", "sau2",  randint(0,850), randint(0,650), listeGress)
spillbrett.opprett_gress("navn3", "gress",  randint(0,850), randint(0,650))
spillbrett.opprett_gress("navn4", "gress",  randint(0,850), randint(0,650))
spillbrett.opprett_stein("navn5", "stein", randint(0,850), randint(0,650))
spillbrett.opprett_stein("navn6", "stein", randint(0,850), randint(0,650))
spillbrett.opprett_ulver("navn7", "ulv", randint(0,850), randint(0,650), listeSauer, listeSteiner)


# Dette er prekode som gjør at pygame zero fungerer. Ikke endre dette:
WIDTH = 900
HEIGHT = 700
def draw():
    screen.fill((128, 81, 9))
    spillbrett.tegn(screen)
def update():
    spillbrett.oppdater()

pgzrun.go()