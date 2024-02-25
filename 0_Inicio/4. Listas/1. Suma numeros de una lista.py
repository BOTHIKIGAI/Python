
"""
11 / 02 /2023

1. Escriba un programa Python para sumar todos los elementos de una lista

"""

num_list = []
# Lista en la cual almacenare los numeros que se sumaran

num = 0
# Variable en la cual se almacena los numeros que seran agregados a la lista

q1 = int(input("Cuantos numeros ingresara a lista: "))
# La variable q1 indicara a los ciclos for el numero de veces que se repiten 

print ("")

# Creo un if por si el usuario ingresa un valor menor a 2
if q1 > 1:

    for x in range(q1):
        # Ciclo For en el cual se ingresa los numeros
        num = float(input("Ingrese numero: "))
        num_list.append(num)
        

    sum = 0.0
    # La variable sum almacenara la suma
    
    for x in range (q1):
        # Inicio un ciclo for el cual se repetira en base a la cantidad de numeros que se ingresara
        sum = sum + num_list[0]
        # Realizo la suma entre la variable sum y la variable que se encuentra en el indice 0 de la variable lista num_list
        num_list.pop(0)
        # Luego de realizar la suma, elimino el indice 0, convirtiendo al numero de indice 1 a indice 0

    print ("La suma de los numeros ingresados es igual a", sum)

elif q1 == 0:
    print ("No tienes ningun numero que ingresar")

else:
    num = float(input("Ingrese numero: "))
    print ("Unicamente ingresaste un dato, por ende la suma es", num)