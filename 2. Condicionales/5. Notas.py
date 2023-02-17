"""
05 / 02 / 2023

5. Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, 
o mostrar "No aprobó" si su nota es menor a 3.0.

"""

import statistics

print ("")
print ("Paso o no paso")
print("")

notas = []
# en la variable "notas" se guarda las notas que seran ingresadas

retomar_pregunta = 0
# la variable "remotar_preguntas" es para controlar el ciclo while

cantidad_notas = int(input("Cuantas notas ingresara? "))

for x in range (cantidad_notas):
    nota = float(input("Ingrese nota: "))
    
    if nota < 0 or nota > 5:
        print("La nota ingresada es menor o mayor que 5, ingrese una nota entre 0.0 y 5.0")
        retomar_pregunta = retomar_pregunta + 1
    else:
        notas.append(nota)

# El ciclo while es creado por las respuestas que se dieron anteriormente, que no fueron respondidas correctamente    

while cantidad_notas > len(notas):

    for x in range(retomar_pregunta):
            nota = float(input("Ingrese nota: "))

            if nota < 0 or nota > 5:
                print("La nota ingresada es menor o mayor que 5, ingrese una nota entre 0.0 y 5.0")
                retomar_pregunta = retomar_pregunta + 1
            else:
                notas.append(nota)


print("")
print ("Las notas ingresadas son las siguiente", notas)
print ("")

if statistics.mean(notas) >= 3.0:
    print ("Aprobo")
else:
    print ("No aprobo")
