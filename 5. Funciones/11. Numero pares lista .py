"""
17 / 02 / 2023

11. Escriba un programa Python para imprimir los números pares de una lista determinada.

"""

def list_num_pares(list):
    indice_x = 0
    list_par = []
    for x in range (len(list)):
        if list[indice_x] % 2 == 0:
            list_par.append(list[indice_x])
            indice_x += 1
        else:
            indice_x += 1
    print (list_par)

list_01 = [0,1,2,3,4,5,6,7,8]
list_num_pares(list_01)