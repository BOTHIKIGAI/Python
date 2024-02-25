import speech_recognition
import pyttsx3
import webbrowser



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
        x = 0

if x == "Institution":
    webbrowser.open("http://serviciosfinancierosena.blogspot.com/")
elif x == "GitHub":
    webbrowser.open("https://github.com/BOTHIKIGAI")
else:
    engine = pyttsx3.init()
    engine.say("Perdon no escuche bien")
    engine.runAndWait()