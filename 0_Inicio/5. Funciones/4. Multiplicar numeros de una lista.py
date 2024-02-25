'''
15 / 02 / 2023

3. Escriba una función de Python para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336

'''

def sum_list(list):
    sum = 1
    while len(list) != 0:
        sum = sum * list[0]
        list.pop(0)
    print (sum)

list = [8, 2, 3, -1, 7]
sum_list(list)