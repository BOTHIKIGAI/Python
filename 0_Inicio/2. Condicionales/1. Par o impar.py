"""
05 / 02 / 2023

1. Solicitar el numero al usuario y determinar si es par, impar o cero


"""

print ("")
print("Hola buen dia, este pequeño programa te dira si un numero es par o impar")
num = float(input("Ingrese el numero: ") )
oper = num % 2

if num == 0:
    print ("El numero ingresado es cero")
elif oper == 1:
    print ("Es impar")
else:
    print ("es par")