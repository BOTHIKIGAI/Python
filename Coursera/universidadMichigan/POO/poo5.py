class PartyAnimal:
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")
    
    # Constructor
    def party(self): # función para modificar parametros
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        
s = PartyAnimal("Sally") # Sally constructed
s.party() # Sally party count 1
j = PartyAnimal("Jim") # Jim constructed
j.party() # Jim party count 1
s.party() # Sally party count 2