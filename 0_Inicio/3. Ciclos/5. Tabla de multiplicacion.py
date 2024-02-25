"""
07 / 02 / 2023

5. Escriba un programa para mostrar la tabla de multiplicar de un entero dado.

"""

num = float(input("Ingrese un numero: "))
mul = 0

for x in range (11):
    print (num, "x", mul, "=",num * mul)
    mul = mul + 1
