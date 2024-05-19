""" 
Programación Orientada a Objetos

En la programación orientadas a objetos (POO), una clase permite
encapsular de forma conjunta atributos (datos) y métodos (acciones).
Cuando una clase sé instancia (crea), da lugar a un objeto.

Por ejemplo, y dada la clase <<coche>>, podemos crear a partir de
ella una instancia objeto que sea un modelo coche determinado
con una matricula concreta. Gracias a los atributos podemos saber
el estado de un objeto. Los metodos de la clase permiten al
objeto realizar acciones y comunicarse con su entorno.
"""

# Ejemplo 1
class Perro:
    
    # Atributo de clase
    especie = 'Mamifero';
    
    # El método __init__ es llamado al crear al objeto
    def __init__(self,nombre,raza):
        print(f"Creando perro {nombre}, {raza}");
        
        # Atributos de instancia
        self.nombre = nombre;
        self.raza = raza;
    
    def ladra(self):
        print("Gua");
    
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Toby", "Bulldog");
print(mi_perro.raza);
mi_perro.camina(10);
mi_perro.ladra();