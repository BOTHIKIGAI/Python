"""
05 / 02 / 2023

4. Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.

"""
print ("")
print ("Quien es mayor, quien es menor")
print("")

num1 = float(input("Ingresa el primer numero: "))
print ("")
num2 = float(input("Ingresa el segundo numero: "))
print ("")

if num1 > num2:
    print (num1,"mayor que", num2)
    print (num2,"menor que", num1)
elif num2 > num1:
    print (num2,"mayor que", num1)
    print (num1,"menor que", num2)
else:
    print("Los numeros son iguales")