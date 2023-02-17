"""
Febrero 01 del 2023

4. Programa que permita calcular la edad de una persona conociendo el año actual y el usuario digita su año de nacimiento.

"""

import datetime


print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer la edad de una persona por medio de su año de nacimiento")

q1 = ""

while q1 != "Si":
    year = int(input("Ingrese el año de nacimiento: "))
    print ("Confirmacion de datos: El año ingresado es correcto ", year)
    q1 = str(input("Si o No: "))
    print("")

date = datetime.date.today()
edad = date.year - year
print ("El individuo tiene" , edad, " años")



