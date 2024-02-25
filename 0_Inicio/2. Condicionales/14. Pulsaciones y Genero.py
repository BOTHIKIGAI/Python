"""
05 / 02 / 2023

15. El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico se calcula con la fórmula:
    
    Género femenino (1): número de pulsaciones = (220 - edad en años)/10
    
    Género masculino (2): número de pulsaciones = (210 - edad en años)/10
    
    Lea la edad y el género y muestre el número de pulsaciones.

"""


print ("")
print ("Pulsaciones y genero")
print("")

edad = int(input("Ingrese la edad: "))
genero = str(input("Ingrese el genero (F para femenino y M para masculino): "))

if genero == "F":
    num_pul = (220 - edad) / 10
elif genero == "M":
    num_pul = (210 - edad) / 10
else:
    print ("Ingresaste un dato incorrecto")