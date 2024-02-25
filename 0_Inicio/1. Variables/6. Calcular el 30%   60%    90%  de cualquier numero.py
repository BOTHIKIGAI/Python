"""
Febrero 01 del 2023

6. Programa que permita calcular el 30%, el 60% y el 90% de cualquier número.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer el 30 [%], 60 [%] y 90 [%] de cualquier numero de entrada ")

q1 = ""

while q1 != "Si":
    print ("Ingrese el numero del cual desea conocer sus porcentajes")
    num = float(input("Numero: "))
    print ("El numero ingresado es correcto (", num ,")")
    q1 = str(input("Si o No: "))

oper1 = 30 * num / 100
oper2 = 60 * num / 100
oper3 = 90 * num / 100

print ("El 30[%] de ", num, " es ", oper1)
print ("El 60[%] de ", num, " es ", oper2)
print ("El 90[%] de ", num, " es ", oper3)