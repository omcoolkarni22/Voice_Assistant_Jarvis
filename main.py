import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def Jarvis_Says(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        Jarvis_Says("I'm Listening to you ")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        Jarvis_Says("I'm recognizing ")
        query = r.recognize_google(audio, language="en-in")
        #print(query)
    except Exception as e:
        print(e)
        Jarvis_Says("Please Say that again!")
        return "None"

    return query


def start():
    hours = int(datetime.now().hour)

    if hours > 0 and hours<12:
        Jarvis_Says("Good Morning !")
    elif hours >=12 and hours < 18:
        Jarvis_Says("Good AfterNoon !")
    else:
        Jarvis_Says("Good Evening !")
    Jarvis_Says("I'm Jarvis , How may I help You , Omkar")


if __name__ == '__main__':
    start()
    while True:
        query = listen().lower()

        if 'wikipedia' in query:
            Jarvis_Says("Gathering some information ... Just a moment ")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Jarvis_Says("According to Wikipedia."+results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search' in query:
            Jarvis_Says("Searching on google")
            query = query.replace("search", "")
            webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'the time' in query:
            time = datetime.now().strftime("%H:%M:%S")
            Jarvis_Says("Sir the time is" + time)

        elif 'open python' in query:
            Jarvis_Says("Starting Pycharm")
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)

        elif 'open java' in query:
            Jarvis_Says("Starting IntelliJ")
            intellij_path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2019.3\\bin\\idea64.exe"
            os.startfile(intellij_path)

        elif 'exit' in query:
            Jarvis_Says("Terminating Code")
            exit()







