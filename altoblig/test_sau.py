from sau import Sau
from sau import Ulv


sau1 = Sau(10, "Klara")
ulv1 = Ulv(10, "Rolf")

assert sau1.lever() == True
assert ulv1.hent_vekt() == 20

ulv1.spis_sau(sau1)
print(sau1.lever())
assert sau1.lever() == False
assert ulv1.hent_vekt() == 25
