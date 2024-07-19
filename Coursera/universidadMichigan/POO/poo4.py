class PartyAnimal:
    def __init__(self):
        self.x = 0
    
    # Constructor
    def party(self): # función para modificar parametros
        self.x = self.x + 1
        print("So far", self.x)
    
    # Desconstructor    
    def __del__(self): # función de eliminación
        print("I am destructed", self.x)

an = PartyAnimal() # instancia de la clase
an.party() # llamada a uno de sus metodos
an.party()
an = 42; # al momento de eliminarlo se ejecuta la función __del__
