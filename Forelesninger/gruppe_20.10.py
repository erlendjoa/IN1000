

class Person:
    def __str__(self):
        return self._name
    def __eq__(self, other):
        return self._farge == other._farge
    def hent_alder(self):
        pass

person1 = Person
person2 = Person
person3 = Person
ordbok = {"p1":person1, "p2":person2, "p3":person3}
for key in ordbok:
    print(f"{key} er {ordbok[key].hent_alder()} år gammel.")
    
person1.__str__()