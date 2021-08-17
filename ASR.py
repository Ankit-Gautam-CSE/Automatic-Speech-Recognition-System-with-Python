import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser
from os import system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(speak):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!") 
    elif hour>=12 and hour<16 :
        speak("Good Afternon!")
    else:
        speak("Good Evening!")
    
    speak("I am gautam . sir , How may i help you...")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gautamankit853@gmail.com','newfriend')
    server.sendemail('gautamankit853@gmail.com','adarsh1183@gmail.com','kamine harami')
    server.close()

if __name__ == '__main__':
    wishMe(speak)
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia....')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query , sentences=3)
        speak("According to wikipedia...")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("goole.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'E:\\gautam all\\old gold\\mp3 songs\\punjabiyon ka craze'
        songs = os.listdir(music_dr)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is{strTime}")

    elif 'open google earth' in query:
        path = "C:\\Program Files\\Google\\Google Earth Pro\\client\\googleearth.exe"
        os.startfile(path)

            





    