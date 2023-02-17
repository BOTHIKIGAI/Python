"""
15 / 02 / 2023

2. Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. 

"""

def numxnum (datoA, datoB):
    print ("El area es de", datoA * datoB, "m2")

# La funcion definida como "numxnum" se usara en aquella figuras en las cuales se obtiene su resultado en base a la multiplicacion de dos datos
# La funcion numxnum aplica a cuadrado, rectangulo, paralelograma

def funcion2 (datoA, datoB):
    print ("El area es de", ((datoA * datoB) / 2), 'm2')

# Para disminuir una linea de codigo decidi ejecutar la operacion directamente en el print
# La funcion "funcion2" aplica a rombo, triangulo, triangulo rectangulo, poligono

def trapecio (datoA, datoB, datoH):
    print ("El area es de", (((datoA + datoB) / 2) * datoH), 'm2')

def triangulo_equilatero (datoA):
    print ("El area es de", (((datoA * datoA) / 4) * (3 ** 0.5)), "m2")


import math

print ("")
print ("Que figura y que area")
print("")

q1 = ""

while q1 != "No":
    
    print("")
    print ("""
    
    Menu
    
    Escribe "A" para saber el area de un rectangulo
    Escribe "B" para saber el area de un cuadrado
    Escribe "C" para saber el area de un paralelogramo
    Escribe "D" para saber el area de un rombo
    Escribe "E" para saber el area de un trapecio
    Escribe "F" para saber el area de un triangulo
    Escribe "G" para saber el area de un triangulo equilatero
    Escribe "H" para saber el area de un triangulo rectangulo
    Escribe "I" para saber el area de un poligono regular
    """)
    
    q2 = str(input("Que clase de area desea conocer: "))

    match q2:
        case "A":
            print ("""
            
                |¯¯¯¯¯¯¯¯¯¯¯¯|
                |            | B
                |____________|
                      A
            """)

            datoA = float(input("Ingrese el lado A: "))
            datoB = float(input("Ingrese el lado B: "))
            numxnum (datoA,datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case "B":
            print ("""
            
                |¯¯¯¯¯¯|
                |      | B
                |______|
                      A
            """)

            datoA = float(input("Ingrese el lado A: "))
            datoB = float(input("Ingrese el lado B: "))
            numxnum (datoA,datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case "C":
            print ("""
            
                   /|¯¯¯¯¯¯¯¯¯/
                  / | h      / 
                 /  |       /
                /___|______/
                    A
            """)

            datoA = float(input("Ingrese el lado A: "))
            datoB = float(input("Ingrese la altura del trapecio: "))
            numxnum (datoA,datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case "D":
            print ("""
                     B
                    /|\  
                   / | \          AC = Distancia entre AC
                  /  |  \         BD = Distancia entre BD
               A /___|___\ C
                 \   |   /
                  \  |  /
                   \ | / 
                    \|/
                     D
            """)

            datoA = float(input("Ingrese la distancia entre AC: "))
            datoB = float(input("Ingrese la distancia entre BD: "))
            funcion2 (datoA, datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case "E":
            print ("""
                    D           C
                   /|¯¯¯¯¯¯¯¯¯¯¯\     h = altura
                  / | h          \    AB = base mayor
                 /  |             \   DC = base menor
                /___|______________\ 
                A                   B
            """)

            datoA = float(input("Ingrese la base menor: "))
            datoB = float(input("Ingrese la base mayor: "))
            datoH = float(input("Ingrese la altura: "))
            trapecio (datoA, datoB, datoH)
            q1 = str(input("Desea conocer otra area (Si o No): "))

        case "F":
            print ("""
                    c           
                   /|\    
                  / |  \            AB   = base
                 /  |h   \          h = altura
                /   |      \ 
               /____|_______\ 
              A     <--->    B
            """)

            datoA = float(input("Ingrese la base: "))
            datoB = float(input("Ingrese la altura: "))
            funcion2 (datoA, datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))

        case "G":
            print ("""
                         .
                        / \  
                       /   \                      
                      /     \ 
                     /       \ 
                L   /         \  L
                   /           \ 
                  /             \ 
                 /               \ 
                /_________________\ 
                        L
            """)

            datoA = float(input("Ingrese el valor de un lado: "))
            triangulo_equilatero (datoA)
            q1 = str(input("Desea conocer otra area (Si o No): "))

        case "H":
            print ("""
            
            |\ 
            |  \                co = cateto opuesto
            |    \              ca = cateto adyacente
            |      \             h = hipotenusa
        co  |        \ h 
            |          \ 
            |            \ 
            |              \ 
            |________________\ 
                    ca
            """)

            datoA = float(input("Ingrese el valor del cateto opuesto: "))
            datoB = float(input("Ingrese el del cateto adyacente: "))
            funcion2(datoA, datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))

        case "I":
            print ("")
            datoA = float(input("Ingrese el valor de uno de sus lados: "))
            datoB = float(input("Ingrese el valor de la apotema: "))
            funcion2(datoA, datoB)
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case _:
            print("")
            print ("Ingresaste un valor que no esta en el menu")



