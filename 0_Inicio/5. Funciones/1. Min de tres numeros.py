"""
15 / 02 / 2023

1. Escriba una funcion en python para encontrar el maximo de tres numeros

"""

def min_function(list):
    while len(list) != 1:
        if list[0] > list [1]:
            list.pop(0)
        else:
            list.pop(1)
    print (list)

list = [4,1,2]
min_function(list)