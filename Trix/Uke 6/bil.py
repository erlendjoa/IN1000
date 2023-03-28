

class Bil:
    def __init__(self, eier):
        self.eier = eier
    def print_eier(self):
        print(self.eier)

ferrari = Bil("Hans")
toyota = Bil("Erlend")
toyota.print_eier()