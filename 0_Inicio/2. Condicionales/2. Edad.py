"""
05 / 02 / 2023

2. Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años mostrar el mensaje "Usted es mayor de edad", de lo contrario "Usted es menor de edad". 
Si el número ingresado es negativo o la edad ingresada es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida.

"""
print ("")
print ("Mayor o menor de edad")
print("")

c1 = 0
# C1 es el variable contador para determminar si el ciclo continua o termina

while c1 == 0:
    edad = int(input("Ingresa tu edad: "))
    if edad <= 0 or edad >= 100:
        print ("Ingresa una edad validad")
        print ("")
    elif edad > 18:
        print ("Eres mayor de edad")
        c1 = 1
    else:
        print ("Eres menor de edad")
        c1 = 1