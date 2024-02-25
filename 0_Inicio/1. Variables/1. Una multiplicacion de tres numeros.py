"""
Enero 31 del 2023

1.	Programa que permita multiplicar 3 números.

"""

import math

contador1 = 0 
num1_list = []

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite multiplicar tres numeros entre si")

while contador1 != 3:
    num = int(input("Ingrese el numero: "))
    num1_list.append(num)
    contador1 = contador1 + 1

result = math.prod (num1_list)
print ("Los numeros a multiplicar son los siguientes", num1_list)
print ("El resultado de esta multiplicacion es el siguiente ", result )


