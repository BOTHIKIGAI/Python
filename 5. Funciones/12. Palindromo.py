''''
18 / 02 / 2023

12. Escriba una funcion en python que compruebe si una cadena pasada es palindromo o no,
    Una palabra o frase que es palindromo se lee igual de izquierda a derecha que de
    derecha a izquierda. Por ejemplo, Ana, Anita lava la tina.

'''

def palindromo(word):
    str(word)
        # Aeguro que el dato ingresado sea un string

    word_mayusculas = word.upper()
        # Hago que todas las letras esten e mayusculas para realizar la comparacion

    list_a = []
        # list_a almacenara la palabra ingresada letra por letra
            # Ejm      palabra = ['W', 'O', 'R', 'D']

    list_b = []
        #list_b almacenara la palabra ingresada letra por letra, pero al reves
            # Ejm      palabra = ['D', 'R', 'O', 'W']

    for x in word_mayusculas:
        list_a.append(x)
            # La letra de la palabra se agregara a la lista
        list_b.insert(0, x)
            # La letra de la palabra se agregara, con la diferencia que la letra agregada al indice 0, por lo cual la palabra quedara al reves
    
    print (list_a)
    print (list_b)

    c = 0
        # C permitira definir el indice que se comparara 
    z = True
        # Dar inicio al ciclo while

    while z == True and c != len(list_a):

            # El ciclo while se ejecutara siempre y cuando z sea True y c sea diferente a la cantidad de letras de la palabra agregada

        if list_a[c] == list_b[c]:
            z = True
            c += 1

            # La variable C permite la evaluacion de cada uno de los indices, por eso sumo mas uno a la variable para su avance

        else:
            z = False
            print('No es un palindromo')

            # El else se ejecutara al momento que el indice x de list_a y list_b sean diferentes, convirtiendo a z en False e imprimiendo
            # No es un palindromo
    
    if z == True:
        print ('Es un palindromo')

            # Al momento que el ciclo while termine a causa de que c sea igual a la cantidad de letras de la palabra ingresada, se evaluara
            # si z sigue siendo True, si lo es se imprimira "Es un palindromo"

palindromo('Ana')
palindromo('Anita lava la tina')
palindromo ('Pelo')