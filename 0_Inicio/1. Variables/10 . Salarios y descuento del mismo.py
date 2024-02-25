"""
Febrero 01 del 2023

10. Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el salario diario y el número de días trabajados. 
Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

"""

print ("")
print ("Buen dia")
print ("Este pequeño programa calcula el salario a pagar y el dinero a descontar del salario")

q1 = ""

while q1 != "Si":
    salario_min = float(input("Ingresa el valor del salario minimo diario: $"))
    dias_work = float(input("Ingrese el numero de dias trabajados: "))
    print ("Los datos ingresados son correctos")
    print ("---------------------------/-------------------------")
    print ("/   Salario minimo diario  /", salario_min)
    print ("---------------------------/-------------------------")
    print ("/   Dias trabajados        /", dias_work)
    print ("---------------------------/-------------------------")
    q1 = str(input("Si o No: "))
    print("")

descontar_pension_y_salud = 25 * (salario_min * dias_work) / 100
# El 15% de salud mas el 10% por concepto de pension es igual a un descuento salarial del 25% (siempre busco ahorrar lineas)

total_pagar = (salario_min * dias_work) - descontar_pension_y_salud
print (" El total a pagar es de $",total_pagar )
