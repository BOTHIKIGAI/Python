"""
05 / 02 / 2023

3.Solicitar número al usuario y determinar si es negativo, positivo o cero.

"""
print ("")
print ("Negativo, cero o positivo")
print("")


# C1 es el variable contador para determminar si el ciclo continua o termina


num = float(input("Ingresa un numero: "))
if num == 0:
    print ("El numero ingresado es un cero (0)")
elif num > 0:
    print ("El numero ingresad0 es positivo")
else:
    print ("El numero es negativo")
    