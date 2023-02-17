"""
Enero 31 del 2023

2.	Solicitar al usuario un número y calcular cuál es el cuadrado del número (2^2=4).

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer el cuadrado de el numero que desee")

q1 = ""

while q1 != "No":
    num = float(input("Ingrese el numero: "))
    resultado = num * num
    print ("El cuadrado de ", num, " es ", resultado)
    q1 = str (input("Desea saber el cuadrado de otro numero (Si o No): " ))
    print ("")