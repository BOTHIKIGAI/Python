'''
15 / 02 / 2023

3. Escriba una función de Python para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20.

'''

def sum_list(list):
    sum = 0
    while len(list) != 0:
        sum = sum + list[0]
        list.pop(0)
    print (sum)

list = [8,2,3,0,7]
sum_list(list)
