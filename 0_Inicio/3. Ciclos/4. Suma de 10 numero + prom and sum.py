"""
07 / 02 / 2023

4. Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.

"""
num = 0
num_s = 0

for x in range (10):
    num = float(input("Ingresa el numero: "))
    num_s = num + num_s

print ("La suma de los diez numeros ingresados es de", num_s, "y el promedio es", num_s / 10)