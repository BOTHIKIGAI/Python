""" 
Herencia
-------------------------------------------------------------------------------
La herencia es un proceso mediante el cual se puede crear una clase hija que
herede de una clase padre, compartiendo sus métodos y atributos. Ademas de
ello, una clase hija puede sobreescribir los metodos o atributos, o incluso
definir unos nuevos.
"""

# Definimos una clase padre
class Animal:
    pass;

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass;

# De hecho podemos ver como efectivamente la clase Perro es la hija de Animal
print(Perro.__base__); # Mediante __base__ se logra saber cual es el padre

# De manera viceversa tambien se puede conocer la descendencia
print(Animal.__subclasses__()); # Mediante __subclasses__ se conoce descendencia