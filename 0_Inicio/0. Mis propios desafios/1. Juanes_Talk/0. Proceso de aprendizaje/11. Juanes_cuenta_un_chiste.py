import speech_recognition
import pyttsx3

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

if x == "sonrisa":
    engine = pyttsx3.init()
    engine.say("¿Por qué las computadoras van al médico?           Porque tienen un virus.")
    engine.say("kkkkkkkk")
    engine.runAndWait()

else:
    engine = pyttsx3.init()
    engine.say("Perdon no entendi la pregunta")
    engine.runAndWait()