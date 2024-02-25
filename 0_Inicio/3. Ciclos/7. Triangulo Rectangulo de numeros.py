"""
07 / 02 / 2023

7. Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:

"""

sum = 1
num = [1]
print (*num)

for x in range (4):
    sum = num[0] + sum
    num.append(sum)
    print (*num)