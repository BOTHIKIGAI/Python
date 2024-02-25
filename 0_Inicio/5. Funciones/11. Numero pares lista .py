"""
17 / 02 / 2023

11. Escriba un programa Python para imprimir los números pares de una lista determinada.

"""

def list_num_pares(list):
    indice_x = 0
        # indice_x es una variable la cual usare para modificar el indice a la hora de filtrar si este es par o impar
    list_par = []
        # list_par almacenara los datos pares de la lista la cual sera examinada
    for x in range (len(list)):
            # Creo un ciclo for el cual iterara n datos de la lista, con el fin de filtrar cada uno de los datos de la lista a examinar
        if list[indice_x] % 2 == 0:
                # Si el indice_x al momento de ser dividido por 2 da como reciduo el resultado de 0, sera un numero par
            list_par.append(list[indice_x])
                # Si el resultado es True se almacenara el dato en list_par
            indice_x += 1
                # EL segundo paso es aumentar la varibale un +1, con el fin de revisar el siguiente indici
        else:
            indice_x += 1
                # Sumar a la variable un +1, y no se agregara a listar_par ninguna variable
    print (list_par)

list_01 = [0,1,2,3,4,5,6,7,8]
list_num_pares(list_01)