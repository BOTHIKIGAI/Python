import random


def ahoracado():

    # QUESTION ABOUT CONTIUES GAME?
    question = "yes"

    while question == "yes":

        # CREATE AN ARRAY WITH WORDS
        palabras = ["amor", "amistad", "familia", "felicidad", "esperanza"]
        # SELECT A RANDOM WORD FROM PALABRAS
        palabra = random.choice(palabras)
        # CREATE AN ARRAY WITH THE NUMER DE LETTER AND THIS ARE DOWN LINES
        letras_adivinadas = ["_"] * len(palabra)
        # CREATE A VARIABLE WHAT HAVE TRY
        intentos = 6

        # WHILE INTENTOS IS GREATER THAN ZERO
        while intentos > 0:

            # JOIN LETRAS DIVINADAS TO MADE A
            print(" ".join(letras_adivinadas))
            letra = input("Adivina una letra: ").lower()

            # CONDITION LENGTH LETRA
            if len(letra) == 1:
                # IF THE LETTER IS INSIDE
                if letra in palabra:
                    if letra in letras_adivinadas:
                        print("Ya adivinaste esta letra")
                    else:
                        for i in range(len(palabra)):
                            if palabra[i] == letra:
                                letras_adivinadas[i] = letra

                else:
                    intentos -= 1
                    print("intentos: ", intentos)

                if "_" not in letras_adivinadas:
                    print("Has ganado! La palabra era: ", palabra)
                    return
            # IF THE LENGTH LETRA IS GREATHER TO 1
            else:
                print("Recuerda que debes ingresar una sola letra y unicamente letra")

        print("Has perdido! La palabra era: ", palabra)
        question = input("¿Deseas continuar? Yes o No: ").lower()

ahoracado()