"""
Febrero 01 del 2023

14. Solicitar al usuario una distancia en metros y transformar a km., cm. o mm.

"""
print ("")
print ("Buen dia")
print ("Este pequeño programa permite transformar metros a km, cm o mm, esto depende de su eleccion.")
print ("")

q1 = ""

while q1 != "No":
    m = float(input("Ingrese el valor en metros: "))
    
    print("")
    print (("Que clase de conversion desea hacer"))
    print ("Escriba 1 si desea pasar de metros a km")
    print ("Escriba 2 si desea pasar de metros a cm")
    print ("Escriba 3 si desea pasar de metros a mm")
    print ("")
    
    q2 = int(input("Que clase de conversion desea hacer: "))

    match q2:
        case 1:
            print ("metros a km")
            print ( m  / 1000, "km")
            q1 = str(input("Deseas hacer otra conversion (Si o No): "))
            print ("")
        case 2:
            print ("metros a cm")
            print ( m * 100, "cm")
            q1 = str(input("Deseas hacer otra conversion (Si o No): "))
            print ("")
        case 3:
            print ("metros a mm")
            print ( m * 1000, "mm")
            q1 = str(input("Deseas hacer otra conversion (Si o No): "))
            print ("")
        case other:
            print ("Ingresaste un valor que no es ni 1, 2 o 3")
