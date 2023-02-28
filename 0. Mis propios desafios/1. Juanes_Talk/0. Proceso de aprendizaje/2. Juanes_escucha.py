import speech_recognition


r = speech_recognition.Recognizer()
    
with speech_recognition.Microphone() as source:
    print("Di algo: ")
    audio = r.listen(source)
    
    try:
        texto = r.recognize_google(audio)
        print ("Tu dijiste {}", format(texto))
        x = ("Tu dijiste {}", format(texto))
    
    except:
        print("Perdon no te puedo escuchar")