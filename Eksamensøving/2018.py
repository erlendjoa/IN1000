

#1a.
#       3
#
#1b.
#       ad
#
#1c.
#       17
#
#1d.
#       9
#
#1e.
#       16
#
#1f.
#       32

#               DEL 1:  6/6


#2a.
#       49
#
#2b.
#       60
#
#2c.    49
#
#2d.
#       49

#               DEL 2: 4/4


#3a.

def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal > bortemaal:
        return hjemmelag
    elif bortemaal > hjemmemaal:
        return bortelag
    else:
        return "uavgjort"


#3b.

def forkort_lagliste(lagliste):
    nyListe = []
    for lag in lagliste:
        if lag not in nyListe:
            nyListe.append(lag)
    return nyListe


#3c.

def legg_inn_null_maal(lagliste):
    lagbok = {}
    for lag in lagliste:
        lagbok[lag] = 0
    return lagbok


#3d.

def ekstraher_lagliste(fn):
    nyListe = []
    for linje in open(fn):
        linje = linje.split()
        nyListe.append(linje[0])
        nyListe.append(linje[1])
    return nyListe


#3e.

def regn_poengsum(fn):

    lagliste = ekstraher_lagliste(fn)
    orglagliste = forkort_lagliste(lagliste)
    lagbok = legg_inn_null_maal(orglagliste)

    for linje in open(fn):
        linje = linje.split()

        lagbok[linje[0]] = linje[2]
        lagbok[linje[1]] = linje[3]
    
    return lagbok


#3f.

def gull(lagoversikt): #ordbok som parameter

    ordboeker_er_krunglete = [[],[]]

    for lag in lagoversikt:
        ordboeker_er_krunglete[0].append(lag)
        ordboeker_er_krunglete[1].append(lagoversikt[lag])

    return vinnerlag(ordboeker_er_krunglete[0][0], ordboeker_er_krunglete[0][1], ordboeker_er_krunglete[1][0], ordboeker_er_krunglete[1][1])


#3g.

def finn_gull(fn):
    
    lagliste = ekstraher_lagliste(fn)
    orglagliste = forkort_lagliste(lagliste)
    lagbok = legg_inn_null_maal(orglagliste)
    print(gull(lagbok))

assert vinnerlag("Brann", "Molde", 2,3) == "Molde"
assert vinnerlag("Brann", "Molde", 1,0) == "Brann"
assert vinnerlag("Brann", "Molde", 2,2) == "uavgjort"

assert forkort_lagliste(["Brann", "Molde", "Brann"]) == ["Brann", "Molde"]

assert legg_inn_null_maal(["Brann", "Molde"]) == {"Brann" : 0, "Molde" : 0}

assert gull({"Brann" : 2, "Molde" : 3}) == "Molde"
assert gull({"Brann" : 4, "Molde" : 3}) == "Brann"

