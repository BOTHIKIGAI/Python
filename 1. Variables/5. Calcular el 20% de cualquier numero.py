"""
Febrero 01 del 2023

5. Programa para calcular el 20% de cualquier número de entrada.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer el 20 [%] de cualquier numero de entrada ")

q1 = ""

while q1 != "Si":
    print ("Ingrese el numero del cual desea conocer su 20%")
    num = float(input("Numero: "))
    print ("El numero ingresado es correcto (", num ,")")
    q1 = str(input("Si o No: "))

oper1 = 20 * num / 100
print ("El 20[%] de ", num, " es ", oper1)