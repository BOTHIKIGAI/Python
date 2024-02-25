"""
16 / 02 / 2023

7. Escriba una función de Python para comprobar si un número cae en un rango determinado.

"""

def tipo_de_dato(dato):
    print ("El dato ingresado es un dato que se encuentra en el rango de", type(dato))

a = 1j
tipo_de_dato(a)

a = 2
tipo_de_dato(a)

a = 'hola'
tipo_de_dato(a)

a = [2,34]
tipo_de_dato(a)

a = {1,2,'kj'}
tipo_de_dato(a)