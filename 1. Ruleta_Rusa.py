"""

28 / 12 / 2022


/////////     /       /   /           /////////   /////////   /////////      /////////     /       /   /////////   /////////
/       /     /       /   /           /               /       /       /      /       /     /       /   /           /       /
/       /     /       /   /           /               /       /       /      /       /     /       /   /           /       /
/////////     /       /   /           /////////       /       /////////      /////////     /       /   /////////   /////////
/       /     /       /   /           /               /       /       /      /       /     /       /           /   /       /
/        /    /       /   /           /               /       /       /      /        /    /       /           /   /       /
/         /   /////////   /////////   /////////       /       /       /      /         /   /////////   /////////   /       /


La ruleta rusa es un juego de azar potencialmente mortal, que consiste en que un jugador coloque una o más balas dentro de un tambor de revólver, gire el cilindro (sin ver en dónde quedó el proyectil), coloque el 
cañón en su sien y presione el gatillo. Se juega generalmente entre dos o más personas. El objetivo es sobrevivir y quedarse con el dinero o la especie de valor a jugar.

Generalmente se inicia en una mesa. Uno de los jugadores toma un revólver (puede ser de 5 o 6 cartuchos) y abre el tambor. En él pone uno o más proyectiles, dependiendo de la cantidad de dinero apostado. Luego gira 
el tambor al azar, cerrándolo rápidamente de modo que ninguno de los jugadores pueda ver en qué recámara se encuentran los cartuchos. Por turnos los jugadores colocan la boca del cañón sobre su sien y aprietan el 
gatillo sin mover el arma. Si ningún cartucho es disparado, el jugador continúa en el juego y el revólver pasa a su compañero. Si el jugador se salva, el revólver es pasado al siguiente jugador hasta que a uno de 
ellos le toque el cartucho y reciba el disparo.


"""

# Pregunta 1 - Iniciamos el Juego

pregunta1 = str(input("Iniciamos el juego? (Si o No): "))

while pregunta1 != "Si" and pregunta1 != "No":
    print("")
    print ("Disculpe, la respuesta dada no es correcta, recuerde que es Si o No")
    pregunta1 = str(input("Iniciamos el juego?: "))

if pregunta1 == "No":
    print("")
    print("Esta bien, nos veremos en otro momento")
else:
    print("")
    print("Perfecto, iniciemos...")

    # Pregunta 2 - Cantidad de Participanes

    print("")
    pregunta2 = int(input("Ingrese la cantidad de participantes, recuerda que debe ser un numero (max. 5): "))
    while pregunta2 <= 0 or pregunta2 >= 6:
        if pregunta2 <= 0:
            print ("Cero participantes?")
            pregunta2 = int(input("Ingrese la cantidad de participantes, recuerda que debe ser un numero (max. 5): "))
        else:
            print ("El numero de participantes maximo es de 5")
            pregunta2 = int(input("Ingrese la cantidad de participantes, recuerda que debe ser un numero (max. 5): "))
    print("")
    
    # Pregunta 3 - Pregunta de Curiosdad - Porque el maximo es de 5 participantes
            
    pregunta3 = str(input("Deseas saber por que el maximo de participantes es de 5? (Si o No): "))

    while pregunta3 != "Si" and pregunta3 != "No":
        print ("Disculpe, la respuesta dada no es correcta, recuerde que es Si o No")
        pregunta3 = str(input("Deseas saber por que el maximo de participantes es de 5? (Si o No): "))
    
    if pregunta3 == "Si":
        print ("La suerte termina en donde empieza...")
    else:
        print ("A veces la ignorancia es mucho mas satisfactoria...")

    # pregunta 4 - El espacio de la bala - En que espacio deseas guardar la bala

    pregunta4 = int(input("En que espacio del tambor desea guardar la bala? (debe ser un numero entre el 1 al 6): "))    

    while pregunta4 <= 0 or pregunta4 >= 7:
        if pregunta1 <= 0:
            print ("Este numero ", pregunta4, " no es posible, puesto debe ser un numero entre el 1 al 6")
            pregunta4 = int(input("En que espacio del tambor desea guardar la bala?"))
        else:
            print ("El numero" , pregunta4, " es muy grande")
            pregunta4 = int(input("En que espacio del tambor desea guardar la bala? (debe ser un numero entre el 1 al 6): "))    
    
    # pregunta 5 - Ingresa 
    
