#while løkker
# while condition: Statement
from random import randint
from random import shuffle

'''
tall=1
while tall<10:
    print(tall)
    tall+=1

sum = 0
x=1
while x<=100:
    sum += x
    x += 1
    print(sum)
'''


kast = 0
suksess = 0
while kast < 1000:
    kast += 1
    terning1 = randint(1,6)
    terning2 = randint(1,6)
    oyne = terning1 + terning2
    print(oyne)
    if oyne >= 10:
        suksess += 1
print(suksess/1000)


linser = ["H", "H", "V", "V"]
ut = 0
suksesser = 0
while ut < 10000:
    ut+=1
    shuffle(linser)
    valg1 = linser[0]
    valg2 = linser[1]
    if valg1 != valg2:
        suksesser+=1
print(suksesser/10000)

print("**********")
#for variable in collection:
#   statement

summen = 0
for tall in [2,3,4]:
    summen+=tall
print(summen)

for tall in range(0,5):
    print(tall*tall)


# prosedyrer med parametre
# subrutiner med returverdi: funksjoner

dusin=12