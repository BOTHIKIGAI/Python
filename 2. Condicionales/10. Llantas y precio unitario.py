"""
05 / 02 / 2023

10. Leer el número de llantas de una compra y mostrar el valor que debe pagarse. El almacén las vende con la siguiente política: Si se compran menos de 6 llantas, 
el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, y si se compran más de 7 llantas, el precio unitario es $180000.

"""


print ("")
print ("Llantas y precio unitario")
print("")

numero_llantas = int(input("Cuantas llantas comprara? "))

if numero_llantas < 6:
    precio = numero_llantas * 240000

elif numero_llantas == 6 or numero_llantas == 7:
    precio = numero_llantas * 221000
    
else:
    precio = numero_llantas * 180000

print ("El precio a pagar por la cantidad de", numero_llantas, "es de", precio)