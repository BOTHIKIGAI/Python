"""
Febrero 01 del 2023

3. Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde x=v*t donde v es velocidad y t es tiempo. Solicitar al usuario velocidad
en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km)

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa le permite conocer la distancia recorrida en km")

q1 = ""

while q1 != "Si":
    velocidad = float(input("Ingrese la velocidad (km/h): "))
    tiempo = float(input("Ingrese el tiempo (Horas): "))
    print ("Los datos son: ", velocidad, " km/h y ", tiempo, "horas" )
    q1 = (str(input("Son correctos (Si o No): ")))
    print("")

print ("La distancia recorrida es de ", velocidad * tiempo, "km")


