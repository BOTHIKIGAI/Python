'''
16 / 02 / 2023

9. Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista.

'''

# Si el caso es crear una lista en la cual se revuelve los valores, si no es asi, pase al siguiente comentario 

def aleatorio_lista (lista):
    import random
    print ('Lista sin modificar', lista)
    random.shuffle(lista)
    print ('Lista modificada', lista)

list = [0,1,2,3,4]
aleatorio_lista(list)

print ("")
print ("")
print ("Segundo caso")

# Si el caso es el de crear una lista con valores de datos no repetidos entonces esta es la solucion

def lista_valores_unicos (lista):
    list_new = set(lista)
    print (list_new)

lista = [2,2,3,4,5,6,1,1,1,8]
lista_valores_unicos(lista)

print ("")