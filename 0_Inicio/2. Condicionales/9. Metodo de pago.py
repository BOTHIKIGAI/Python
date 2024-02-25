"""
05 / 02 / 2023

9. Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 
pago con el celular (dinero electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Caso contrario, pago con la tarjeta de crédito.

"""


print ("")
print ("Dinero")
print("")

dinero = float(input("Cuanto dinero es? "))

if dinero < 150000: 
    print ("El metodo a usar para realizar el pago es en efectivo")
elif dinero >= 150000 and dinero <= 300000:
    print ("El metodo a usar para realizar el pago es pago con celular") 
else:
    print ("El metodo a usar para realizar el pago es pago con tarjeta de debito")
