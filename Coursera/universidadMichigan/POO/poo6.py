# clase padre
class PartyAnimal:
    
    # constructor
    def __init__(self, nam):
        self.x = 0 # propiedad autonicializada
        self.name = nam # propiedad nombre
        print(self.name, "constructed") # imprime el nombre
    
    # metodo
    def party(self):
        self.x = self.x + 1; # aumenta la propiedad x
        print(self.name, "party count", self.x) # imprime nombre y la propiedad x

# clase hija
class FootballFan(PartyAnimal): # Hereda del padre PartyAnimal
    
    # constructor
    def __init__(self, nam):
        super().__init__(nam) # trae las propiedad de la clase padre
        self.points = 0 # los puntos se inicializan en 0
    
    # metodo
    def touchdown(self):
        self.points = self.points + 7 # aumenta la propiedad de puntos
        self.party # llama el metodo heredado del padre
        print(self.name, "points", self.points) # imprime 

# instanciar clases
s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()