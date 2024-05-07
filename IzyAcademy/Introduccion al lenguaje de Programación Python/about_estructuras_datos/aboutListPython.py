""" List """

""" 
Las listas son estructuras de datos que contienen una colección
ordenada de elementos. Estos elementos son generalmente del mismo
tipo y pueden contener elementos como tipos de datos individuales
u otras estructuras de datos más complejas como listas, diccionarios, etc.

Las listas se usan comunmente en la programación para almacenar y organizar
datos para que puedan ordenarse, indexarse o buscarse fácilmente.

Las listas se asignan a las variables usando un solo igual, se denotan
entre corchetes y usan una coma para separar los elementos.
"""

L = [20, "Juan", 20.9, [30, 40, 50]];
print(L); # mediante print se lista todos los elementos
 
""" Agregar un elemento a la lista  """
milan = ["Gato", 2];
milan.append("Gris"); # mediante el metodo append se puede agregar un dato a la lista
print(milan); 

""" Remplazar elemento de una lista """
milan[2] = "Atigrado gris";
print(milan);

""" Remover un elemento de una lista """
milan.pop(1);
print(milan);

""" Unir dos listas """
tara = ["Gato", "Blanca", "Anaranjada", ];
gatos = [];
gatos.insert(-1,tara);
gatos.insert(-1,milan);
print(gatos);

""" Acceder a elementos de una lista """
print(tara[0]); # acceder a un elemento en especifico
print(tara[0:3]); # accede al rango de elementos
print(tara[:2]); # accede hasta ese valor
print(tara[-1]); # acceder en de derecha a izquierda con el negativo