import speech_recognition
import pyttsx3
import datetime
import calendar

r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Di algo: ")
    audio = r.listen(source)
    
    try:
        texto = r.recognize_google(audio)
        print ("Tu dijiste {}", format(texto)) 
        z = (format(texto)) 


    except:
        print("Perdon no te puedo escuchar")

if z == "Dia de hoy":
    fecha_actual = datetime.datetime.now()
    mes_actual_num = fecha_actual.month
    mes_actual_str = calendar.month_name[mes_actual_num]
    engine = pyttsx3.init()
    engine.say ("Hoy es")
    engine.say (fecha_actual.strftime("%d de {} de %Y").format(mes_actual_str))
    engine.runAndWait()
            
else:
    engine = pyttsx3.init()
    engine.say("Perdon no escuche bien")
    engine.runAndWait()