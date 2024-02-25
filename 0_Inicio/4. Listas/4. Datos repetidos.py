"""
12 / 02 / 2023

4. Escriba un programa Python para eliminar duplicados de una lista.

"""

list = []
# List almacenara los datos que se ingresaran

q1 = int(input("Cuantos datos ingresara: "))
# q1 indicara al ciclo for el numero de repeticiones que este debe hacer

if q1 > 1:
    for x in range(q1):
        dato = input("Ingrese el dato deseado: ")
        list.append(dato)
        print (list)

    a = 0

    for x in range(q1):
        if list.count(list[a]) == 2:
            list.remove(list[a])
            a = a + 1
    
    while q1 != 0:
        if list.count(list[a]) >= 2:
            list.remove(list[a])

    print (list)


else:
    print ("Datos insuficientes para ejecutar el codigo") 
