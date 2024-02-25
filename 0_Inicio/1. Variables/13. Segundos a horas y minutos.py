"""
Febrero 01 del 2023

13.	Solicitar tiempo en segundos y transformar a horas y minutos.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa permite transformar los segundos a horas y minutos")
print ("")

q1 = ""

while q1 != "Si":
    seg = float(input("Ingresa los segundos: "))
    print ("El valor ingresado es correcto: ", seg, "segundos" )
    q1 = str(input("Si o No: "))

print ("La cantidad de segundos en horas es igual a ", seg / 3600, "H y la cantidad de segundos en minutos es igual a ", seg / 60, "min")