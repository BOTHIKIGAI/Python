""""
06 / 02 / 2023

Ejercicio 12
Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento. Si compra más de 5 artículos, pero menos de 10, 
el precio unitario se reduce en 5%. Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio unitario original. 
Calcule y muestre el valor total a pagar.

"""


buy_cantidad = int(input("Ingrese la cantidad de compras hechas: "))
total_pagar_sd = 0
total_pagar_cd = 0

for x in range (buy_cantidad):
    precio = float(input("Ingrese el precio: "))
    total_pagar_sd = precio + total_pagar_sd

if buy_cantidad > 5 and buy_cantidad < 10:
    descuento = total_pagar_sd * (buy_cantidad * 5) / 100
    print ("El descuento es de", descuento)
    print ("El total a pagar es de ", total_pagar_sd - descuento)
elif buy_cantidad > 10:
    descuento = total_pagar_sd * (buy_cantidad * 8) / 100
    print ("El descuento es de", descuento)
    print ("El total a pagar es de ",total_pagar_sd - descuento)