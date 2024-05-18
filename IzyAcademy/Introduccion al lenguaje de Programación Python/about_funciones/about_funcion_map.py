""" 
Funcion map
----------------------------------------------------------------------
La funciòn map() en python es una funciòn incorporada que se utiliza
para aplicar una funciòn especifica a cada elemento de un iterable
(como una lista, tupla, etc.) Esta función devuelve un objeto
mapeador, que es un iterador que contiene los resultados de aplicar
la función a cada elemento del iterador original.
"""

# Se define una función para su reutilización
def cube(numero):
    return numero**3;

numeros = list(map(cube,([3,6,10])));
print(numeros);
"""
Instanciamos una vairable la cual sera una lista que usara la función
map() para recorrer cada elemento de una lista.
"""