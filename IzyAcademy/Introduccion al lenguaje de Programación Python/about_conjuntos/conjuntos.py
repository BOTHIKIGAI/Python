""" Conjuntos """
""" 
Los conjuntos son una colección no ordenada y sin elementos repetidos, utiles
si queremos almacenar información unica. Tambien debemos saber que los
conjuntos son inmutables, por lo tanto, no podemos modificar el valor de un
elementos.
"""

numeros = {1,2,4,5,6,7,8,9,10}; # Un conjunto se define con corchetes
print(numeros);

ingredientes_tinto = {"panela", "agua", "cafe"};
print(ingredientes_tinto);

list_numeros = [1,2,2,3]; # iniciamos una lista con elementos repetidos
set_numeros = set(list_numeros); # La convertimos a un conjunto
print(set_numeros); # Imprimimos el conjunto para observar que los datos repetidos ya no estan

""" Agregar elementos a un conjunto """

set_numeros.add(4); # añadir un valor
print(set_numeros);
set_numeros.update([8,6,5]); # añadir multiples valores
print(set_numeros);

""" Remover elementos de un conjunto """

set_numeros.remove(2); # Remover un valor
set_numeros.pop(4); # Remover un valor mediante pop
