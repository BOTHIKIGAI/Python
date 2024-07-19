"""
5.2 Escriba un programa que pida repetidamente números
enteros a un usuario hasta que éste introduzca "hecho".
Una vez introducido "hecho", imprime el mayor y el menor
de los números.  Si el usuario introduce algo que no sea
un número válido, captúralo con un try/except, emite un
mensaje apropiado e ignora el número. Introduce 7, 2, bob,
10, y 4 e iguala la salida de abajo.
"""

largest = 0
smallest = None
num = 0
control = True

while control:

    try:
        num = input("Enter a number: ")
        if num == "done":
            control = False
            print("Maximum is", largest)
            print("Minimum is", smallest)
            break
        else:
            num = int(num)
            largest = num if num > largest else largest
            smallest = largest if smallest is None else num if num < smallest else smallest

    except:
        print("Invalid input")

