'''
16 / 02 / 2023

8. Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 

'''

def may_min_palabras(palabra):
    
    list_letra = []
    
    b = 0
    c = 0

    for letra in palabra:
        list_letra.append(letra)
    
    while len(list_letra) != 0:
        if list_letra[0].isupper():
            b += 1
            list_letra.pop(0)
        else:
            c += 1
            list_letra.pop(0)

    print ("La palabra", palabra, "tiene", b, "letras en mayusucula y", c, "letras en minuscula")


palabra = input('Ingresa la palabra: ')
may_min_palabras(palabra)