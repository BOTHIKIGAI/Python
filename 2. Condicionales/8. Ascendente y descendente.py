"""
05 / 02 / 2023

8. Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. 
"""


print ("")
print ("Ascendente y descendente")
print("")

num_list = []

for x in range(3):
    num = float(input("Ingrese numero: "))
    num_list.append(num)
    print(num_list)

print ("Numeros ingresados sin modificar el orden:", num_list)

num_list.sort()

print ("Numero ingresados de menor a mayor:", num_list)

num_list.sort (reverse=True)

print ("Numero ingresados de mayor a menor", num_list)
