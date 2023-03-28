def prosedyre(x):
    svar = x+2
    return svar

def prosedyre2(x):
    if x > 10:
        return True
    else:
        return False

var1 = (prosedyre(3))
print(var1)

prosedyre2(8)

print("*****")

def test():
    liste = [1, 2, 3, 4, 5, 6]
    for element in range(len(liste)):
        print(liste[element])
test()
