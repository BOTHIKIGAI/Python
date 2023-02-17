"""
Febrero 01 del 2023

12. Calcular la hipotenusa con el Teorema de Pitágoras.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa descubre la hipotenusa de un triangulo")


q1 = ""

while q1 != "Si":
    print ("No te preocupes por el orden de los catetos")
    print ("")
    co= float(input("Ingrese el cateto opuesto: "))
    ca = float(input("Ingrese el cateto adyacente: "))

    print ("Los datos ingresados son correctos")
    print ("---------------------------/-------------------------")
    print ("/   Cateto Opuesto         /", co)
    print ("---------------------------/-------------------------")
    print ("/   Cateto Adyacente       /", ca)
    print ("---------------------------/-------------------------")

    q1 = str(input("Si o No: "))
    print("")

print ("La hipotenusa tiene un valor de ", ((ca * ca) + (co * co)) ** 0.5)
