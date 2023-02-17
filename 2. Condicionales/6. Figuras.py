"""
05 / 02 / 2023

6. Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio).

"""

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

            A = float(input("Ingrese el lado A: "))
            B = float(input("Ingrese el lado B: "))
            print ("El area del rectangulo es", A * B, "m2")
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case "B":
            print ("""
            
                |¯¯¯¯¯¯|
                |      | B
                |______|
                      A
            """)

            A = float(input("Ingrese el lado A: "))
            B = float(input("Ingrese el lado B: "))
            print ("El area del cuadrado es", A * B, "m2")
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case "C":
            print ("""
            
                   /|¯¯¯¯¯¯¯¯¯/
                  / | h      / 
                 /  |       /
                /___|______/
                    A
            """)

            A = float(input("Ingrese el lado A: "))
            B = float(input("Ingrese la altura del trapecio: "))
            print ("El area del paralelogramo es", A * B, "m2")
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

            A = float(input("Ingrese la distancia entre AC: "))
            B = float(input("Ingrese la distancia entre BD: "))
            print ("El area del rombo es",((A * B)/ 2), "m2")
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

            A = float(input("Ingrese la base menor: "))
            B = float(input("Ingrese la base mayor: "))
            h = float(input("Ingrese la altura: "))
            print ("El area del trapecio es",(((A + B) / 2) * h), "m2")
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

            A = float(input("Ingrese la base: "))
            B = float(input("Ingrese la altura: "))
            print ("El area del triangulo es",((A * B) / 2), "m2")
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

            A = float(input("Ingrese el valor de un lado: "))
            print ("El area del triangulo equilatero es", (((A * A) / 4) * (3 ** 0.5)), "m2")
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

            A = float(input("Ingrese el valor del cateto opuesto: "))
            B = float(input("Ingrese el del cateto adyacente: "))
            print ("El area del triangulo rectangulo es", ((A * B) / 2), "m2")
            q1 = str(input("Desea conocer otra area (Si o No): "))

        case "I":
            print ("")
            A = float(input("Ingrese el valor de uno de sus lados: "))
            B = float(input("Ingrese el valor de la apotema: "))
            print ("El area del poligono regular es", ((A * B) / 2), "m2")
            q1 = str(input("Desea conocer otra area (Si o No): "))
        
        case _:
            print("")
            print ("Ingresaste un valor que no esta en el menu")