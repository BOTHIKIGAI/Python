"""
27 / 02 / 2023

Juanes_talk, es el nombre del asistente que he estado programando con las diferentes librerias, esta programada para responder a diferentes
preguntas ya determinadas

"""

import pyttsx3
    # pyttsx3 libreria se reproduce audio
import speech_recognition
    # speech_recognition libreria de reconocimiento de voz
import pywhatkit
    # pywhatkit libreria para la reproduccion de video por medio de youtube y enviar mensajes a youtube

import datetime
    # datetime proporciona clases para manipular fechas y horas
import calendar
    # calendar proporciona clases para trabajar con fechas, gestionar valores orientados a años / mes / semana 
import webbrowser
    # webbrowser es un navegador web, haciendo uso de la funcion open()
from playsound import playsound

playsound('y2mate.com - Microsoft Windows XP sonido de inicio.mp3')


engine = pyttsx3.init()
engine.say("Mucho gusto soy Juanes talk")
engine.runAndWait()


print ("""

Las preguntas que puedes hacerle a Juanes_talk son las siguientes

1. Preguntas y Respuestas                               2. Chiste - comando de voz = sonrisa
    - comando de voz = hola como estas
    - comando de voz = musica buena
    - comando de voz = dia de hoy

3. Abrir pagina web                                                     4. Reproducir musica
    - comando de voz = Institution                                         - comando de voz = amor
        (abre la pagina del SENA CSF)                                        (cancion de Juanes - Amores prohibidos)
    - comando de voz = GitHub                                              - comando de voz = triste
        (abre el inicio del repositorio de GitHub de BOTHIKIGAI)             (cancion de Ed Maverick - Fuentes de Ortiz)
                                                                           - comando de voz = estudia
                                                                  
                                                                                        (musica para estudiar)
                                                                                  
5. Mensajes Whatsapp                                                     
    - comando de voz = saludo mama                                        
    - comando de voz = saludo Papa                                           
    - comando de voz = saludo Grupo                                        

""")


continuar = 1

while continuar == 1:

    r = speech_recognition.Recognizer()
        
    with speech_recognition.Microphone() as source:
        print("Di algo: ")
        audio = r.listen(source)
        
        try:
            texto = r.recognize_google(audio)
            print ("Tu dijiste {}", format(texto)) 
            x = (format(texto)) 

        except:
            print("Perdon no te puedo escuchar")
    
    if x == "hola como estas":
        engine = pyttsx3.init()
        engine.say("estoy bien, gracias por preguntar")
        engine.runAndWait()

    elif x == "musica Buena":
        engine = pyttsx3.init()
        engine.say("Juanes , Feid, Carlos Vives, Rammstein")
        engine.runAndWait()

    elif x == "Dia de hoy":
        fecha_actual = datetime.datetime.now()
        mes_actual_num = fecha_actual.month
        mes_actual_str = calendar.month_name[mes_actual_num]
        engine = pyttsx3.init()
        engine.say ("Hoy es")
        engine.say (fecha_actual.strftime("%d de {} de %Y").format(mes_actual_str))
        engine.runAndWait()

    elif x == "sonrisa":
        engine = pyttsx3.init()
        engine.say("¿Por qué las computadoras van al médico?           Porque tienen un virus.")
        engine.say("kkkkkkkk")
        engine.runAndWait()

    elif x == "Institution":
        webbrowser.open("http://serviciosfinancierosena.blogspot.com/")
        engine = pyttsx3.init()
        engine.say("Abriendo la pagina del Centro de Servicios Financieros del SENA")
        engine.runAndWait()

    elif x == "GitHub":
        webbrowser.open("https://github.com/BOTHIKIGAI")
        engine = pyttsx3.init()
        engine.say("Abriendo GitHub")
        engine.runAndWait()

    elif x == "amor":
        pywhatkit.playonyt("juanes amores prohibidos")
        engine = pyttsx3.init()
        engine.say("Reproduciendo amores prohibidos de Juanes")
        engine.runAndWait()

    elif x == "triste":
        pywhatkit.playonyt("https://www.youtube.com/watch?v=PaoCQHwTPg4")
        engine = pyttsx3.init()
        engine.say("Reproduciendo Fuentes de Ortiz de Ed Maverick")
        engine.runAndWait()

    elif x == "estudia":
        pywhatkit.playonyt("https://www.youtube.com/watch?v=9CL34BQxmEs")
        engine = pyttsx3.init()
        engine.say("Que comience el estudio")
        engine.runAndWait()

    elif x == "saludo mama":
        hora = int(input("A que hora desea enviar el mensaje: "))
        min = int(input("En que minuto desea enviar el mensaje: "))
        pywhatkit.sendwhatmsg("+57", "Hola mama, como estas ?", hora, min)
        engine = pyttsx3.init()
        engine.say("Enviando mensaje mama")
        engine.runAndWait()

    elif x == "saludo Papa":
        hora = int(input("A que hora desea enviar el mensaje: "))
        min = int(input("En que minuto desea enviar el mensaje: "))
        pywhatkit.sendwhatmsg("+57", "Hola papa, como estas ?", hora, min)
        engine = pyttsx3.init()
        engine.say("Enviando mensaje papa")
        engine.runAndWait()

    else:
        engine = pyttsx3.init()
        engine.say("Perdon no entendi el comando")
        engine.runAndWait()
    
        r = speech_recognition.Recognizer()

    continuar = int(input("Desea realizar otra pregunta: Si = 1 , No = 2:  "))


engine = pyttsx3.init()
engine.say("Juanes talk se despide")
engine.runAndWait()
playsound('Microsoft Windows XP sonido de inicio.mp3')
