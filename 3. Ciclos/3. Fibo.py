"""
07 / 02 / 2023

3. Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).

"""

repetecion = int(input("Cuantas repeticiones desea hacer?: "))

n1 = 0
n2 = 1
n3 = 0

print (n1)
print (n2)

for x in range (repetecion):
    n3 = n1 + n2
    print (n3)
    n1 = n2 + n3
    print (n1)
    n2 = n3 + n1
    print (n2)