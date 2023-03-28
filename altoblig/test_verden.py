from verden import Verden

v1 = Verden()
v1.opprett_dyr("Sau", "Klara", 3)
v1.opprett_dyr("Sau", "Jonas", 5)
v1.opprett_dyr("Ulv", "Bingus", 9)
v1.opprett_dyr("Ulv", "Floppa", 8)

assert v1.antall_sauer() == 2
assert v1.antall_ulver() == 2
v1.beskriv()

v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
v1.oppdaterer()
print(v1.finn_feiteste_ulv())