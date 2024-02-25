"""
12 / 02 / 2023

3. Escriba un programa Python para obtener el número más pequeño de una lista.

"""

num_list = []
# num_list es una lista en la cual almacenare los numeros

num = 0.0
# num es la variable que se usara para agregar datos a una lista

q1 = int(input("Cuantos numeros se ingresaran: "))
# q1 delimitara los ciclos for para realizar las repeticiones en los ciclos for

if q1 > 1:
    for x in range(q1):
        # ciclo for para ingresar los datos a num_list
        num = float(input("Ingrese numero: "))
        num_list.append(num)
        print (num_list)
    
    while len(num_list) != 1:
        # ciclo while para realizar las comparaciones, se dentendra cuando la lista num_list tenga unicamente un dato
            if num_list[0] > num_list[1]:
                num_list.pop(0)
            else:
                num_list.pop(1)
        
    print ("El menor de los numeros ingresados es", *num_list)

elif q1 == 1:
    num = float(input("Ingrese numero: "))
    print ("El menor de los numeros ingresados es", num)

else:
    print("No tienes numeros para ingresar")