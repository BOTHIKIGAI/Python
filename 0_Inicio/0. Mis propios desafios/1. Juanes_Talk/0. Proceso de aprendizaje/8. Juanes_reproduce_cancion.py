import speech_recognition
import pyttsx3
import pywhatkit

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

if x == "amor":
    pywhatkit.playonyt("juanes amores prohibidos")
elif x == "triste":
    pywhatkit.playonyt("https://www.youtube.com/watch?v=PaoCQHwTPg4")
elif x == "estudiar":
    pywhatkit.playonyt("https://www.youtube.com/watch?v=9CL34BQxmEs")
else:
    engine = pyttsx3.init()
    engine.say("Perdon no entendi la pregunta")
    engine.runAndWait()
