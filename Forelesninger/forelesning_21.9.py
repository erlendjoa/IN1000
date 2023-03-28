

def lagOrdbok(navn):
    ordbok = {}

    fil = open(navn, "r")

    for linje in fil:
        data = linje.strip().split(" ")
        key = data[0]
        value = float(data[1])
        ordbok[key] = value

    return ordbok

print(lagOrdbok("Forelesninger/varer.csv"))


