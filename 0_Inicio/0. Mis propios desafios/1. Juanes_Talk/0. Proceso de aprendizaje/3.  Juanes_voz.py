import speech_recognition
import pyttsx3

r = speech_recognition.Recognizer()
    
with speech_recognition.Microphone() as source:
    print("Di algo: ")
    audio = r.listen(source)
    
    try:
        texto = r.recognize_google(audio)
        print ("Tu dijiste {}", format(texto))
            
    except:
        print("Perdon no te puedo escuchar")


engine = pyttsx3.init()
engine.say(("Tu dijiste {}", format(texto)))
engine.runAndWait()