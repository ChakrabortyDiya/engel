import webbrowser
import os
import speech_recognition as sr
import wikipedia
import pyttsx3 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

