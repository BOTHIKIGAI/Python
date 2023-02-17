"""
Febrero 01 del 2023

8. Programa que permita ingresar 5 números y calcular el promedio.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer el promedio de 5 numeros")

import statistics
cont = 0
numlist = []

for x in range (5):
    cont = cont + 1
    num = float(input("Ingrese el numero: "))
    numlist.append(num)
    print(numlist)

promedio = statistics.mean(numlist)
print ("El promedio de los numeros ingresados", numlist, " es de ", promedio )