"""
Febrero 01 del 2023

7. Programa para calcular el área de un cuadrado, la longitud de un lado la ingresa

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer el area de un cuadrado")

q1 = ""

while q1 != "Si":
    num = float(input("Ingrese el lado del cuadrado: "))
    medida = str(input("Ingresa la medida (ejm. cm, m, etc): "))
    print ("El numero ingresado es correcto (", num ,")")
    q1 = str(input("Si o No: "))
    print("")

area = num * num
print ("El area del cuadrado es ", area, medida,"2")