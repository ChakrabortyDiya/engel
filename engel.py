import webbrowser
import os
import speech_recognition as sr
import wikipedia
import pyttsx3 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")

    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    
    return query

if __name__ == '__main__':
     speak("Engel is here ")
     speak("How can i help you")
while True