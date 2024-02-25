"""
07 / 02 / 2023

8. Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1.

"""

# 0 1 2 3 4 5 6
#       1
#      2 3
#     4 5 6
#    7 8 9 10


lineas = 4
lim1 = 0

for x in range(1, lineas +1):

    for z in range(lineas - x):
        print(" ", end="")

    for z in range(1, x+1):
        lim1 = lim1+1
        print(f"{lim1} " , end="")

    print()