""" Diccionarios de datos """
""" 
    Los diccionarios son estructuras de datos que contienen una colección de pares de "clave" 
    y "valor" donde cada clave debe ser una cadena única y el valor puede variar desde una sola 
    variable hasta otras estructuras de datos (como otro diccionario, una lista o tupla).

    Si intenta agregar un nuevo par clave:valor cuando la clave ya existe en el Diccionario, 
    debería obtener un error KeyExists o correr el riesgo de sobrescribir los datos existentes.

    Los diccionarios se usan comúnmente para almacenar y organizar datos para que puedan clasificarse, 
    indexarse o buscarse fácilmente.

    Los diccionarios son mutables, por lo tanto, podemos agregar, cambiar o eliminar elementos.

    Los diccionarios se asignan a las variables usando un solo igual (=) y se indican con corchetes, 
    usando la coma para separar los elementos y dos puntos para separar la clave y el valor.
"""

curso = {
    'nombre' : 'programación de python',
    'duracion' : 50,
    'alumnos' : ['Juanes', 'Niyi', 'Milan', 'Tara']
}

curso['temas'] = ['variables', 'estructuras de datos', 'condicionales']; # insertar un nuevo clave valor en el diccionario
print(curso); # imprime toda la información
print(curso['alumnos']); # imprime unicamente los valores de la clave alumnos

""" Eliminar elementos de un diccionario """

# El metodo utilizado es .pop("key") indicando la clave del elemento

curso['gatos'] = ['pacho', 'anubis', 'tabata']; # se agregaron datos que no corresponden al diccionario
print(curso); # imprimimos como esta actualmente el diccionario
curso.pop('gatos'); # eliminamos la clave-valor gatos
print(curso); # imprimimos para visualizar la eliminación}

""" Obtener los valores de un diccionario mediante la llave (key) """
""" 
    Existen dos maneras para obtener los valores de una key el primero es mediante
    el nombre del diccionario y la llave, curso['temas'], el otro es mediante
    el nombre del diccionario y el metodo .get("llave").

    El get en caso de que no encuentre la llave nos retornara none, en cambio sin el
    metodo nos dara error.
"""

print(curso['temas']);
print(curso.get('temas'));

""" Obtener todas las claves o elementos de un diccionario """

# Para acceder a todas las claves de un diccionario se usa el metodo .keys()
# Para acceder a todos los valores de un diccionario se usa el metodo .values()

print(curso.keys(), type(curso.keys())); # mediante el meotod keys sabremos las llaves del diccionario}
list_keys = list(curso.keys()); # dentro de una vairable que sera una lista ingresamos las llaves
print(list_keys); # imprimimos la variables

print(curso.values()); # mediante values sabremos todos los valores del diccionario
list_values = list(curso.values()); # los valores de curso quedan en una lsita dentro list_values
print(list_values);