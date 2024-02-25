"""
05 / 02 / 2023

12. El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:

/--------------//--------------/
/    Tamaño    /     Precio    /
/--------------//--------------/
/              //              /
/      1       //    $15000    /
/              //              /
/--------------//--------------/
/              //              /
/      2       //    $24000    /
/              //              /
/--------------//--------------/
/              //              /
/      3       //    $36000    /
/              //              /
/--------------//--------------/

Si cada ingrediente adicional cuesta $4.000. Escribir un programa que solicite al empleado encargado de registrar las ventas, 
el tamaño de la pizza y el número de ingredientes adicionales y muestre al cliente el precio que debe pagar.

"""

print ("")
print ("Pizza y precio")
print("")

print ("""

/--------------//--------------/
/    Tamaño    /     Precio    /
/--------------//--------------/
/              //              /
/      1       //    $15000    /
/              //              /
/--------------//--------------/
/              //              /
/      2       //    $24000    /
/              //              /
/--------------//--------------/
/              //              /
/      3       //    $36000    /
/              //              /
/--------------//--------------/

""")

tamaño = int(input("Ingresa el tamaño de la pizza (1,2 o 3): "))
ingredientes = int(input("Ingresa la cantidad de ingredientes: "))

if tamaño == 1:
    total_pagar = 15000 + (4000 * ingredientes)
elif tamaño == 2:
    total_pagar = 24000 + (4000 * ingredientes)
elif tamaño == 3:
    total_pagar = 36000 + (4000 * ingredientes)
else:
    print("Ingresas un tamaño no registrado")

print ("El total a pagar por la pizza de tamaño", tamaño, "y con un total de", ingredientes, "ingredientes, es de $", total_pagar)