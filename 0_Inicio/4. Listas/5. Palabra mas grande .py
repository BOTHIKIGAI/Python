"""
13 / 02 / 2023

5. Escriba un programa Python para encontrar la lista de palabras que son mas largas que n de una lista dada de palabras

"""

list_palabras = []
# list_palabras almacenara los palabras que seran ingresadas

repeticiones = int(input("Cuantos datos ingresara? "))
# repeticiones indicara el numero de veces que el ciclo for debera repetirse para ingresar la cantidad de palabras deseadas

# creo un condicional en base a la respuesta de ingresada en la variable repeticiones
if repeticiones > 1:

    # El ciclo for se repetira x veces para ingresar los datos solicitados
    for x in range (repeticiones):
        palabra = input("Ingrese el dato: ")
        str(palabra)
        list_palabras.append(palabra)

    while repeticiones != 1:
        repeticiones = repeticiones - 1
        


else:
    print("Cantidad de datos insuficientes para la ejecucion del codigo")