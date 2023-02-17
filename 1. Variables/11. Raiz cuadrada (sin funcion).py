"""
Febrero 01 del 2023

11. Programa que solicite un número al usuario y permita calcular la raíz cuadrada del mismo (sin usar función).

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa descubre la raiz cuadrada sin necesidad de usar la funcion")

q1 = ""

while q1 != "Si":
    num = float(input("Ingrese el numero: "))
    print ("El valor ingresado es correcto: ", num )
    q1 = str(input("Si o No: "))
    print("")

raiz = num ** 0.5
# ** el doble asterisco es para realizar una potenciacion de 1/2 con el 0.5, recordemos que la raiz seria lo contrario a la potenciacion

print ("La raiz de", num, "es", raiz)