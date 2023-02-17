"""
Febrero 01 del 2023

9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. 
Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa hace uno de los funcionamientos basicos de una caja de tienda")

q1 = ""

while q1 != "Si":
    valor_unitario = float(input("Ingrese el valor unitario del producto: "))
    cantidad_producto = int(input("Ingrese la cantidad comprada del mismo producto: "))
    print ("Los datos ingresados son correctos")
    print ("-------------------------/------------------")
    print ("/   valor unitario       /", valor_unitario)
    print ("-------------------------/------------------")
    print ("/   cantidad             /", cantidad_producto)
    print ("-------------------------/------------------")
    q1 = str(input("Si o No: "))
    print("")

iva = 16 * (valor_unitario * cantidad_producto) / 100
valor_final = (valor_unitario * cantidad_producto) + iva
print ("El total a pagar es de $", valor_final)