import pyttsx3
import datetime
import speech_recognition as SR
import wikipedia as wiki
import webbrowser
import os
import smtplib
import numpy as np


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour >= 12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('I am David? How may i help you?')

def takeCommand():
    '''It takes microphone input from user and returns string output'''
    reco = SR.Recognizer()
    with SR.Microphone() as source:
        print('Listening...')
        reco.pause_threshold = 1
        audio = reco.listen(source)

    try:
        print("Recognizing...")
        query = reco.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return 'None'
    return query

def sendEmail(to,content):
    fileName = 'pass.txt'
    data = np.loadtxt(fileName, dtype=str)
    print(data)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", data)
    server.send("youremail@gmail.com",to,content)
    server.close()

if __name__=="__main__":
    # speak("Kanishq is a good boy")
    wishMe()
    

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia","")
            results = wiki.summary(query,sentences = 2)
            print(results)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")
        elif 'open gmail' in query:
            speak('Opening Gmail')
            webbrowser.open("gmail.com")
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")
        elif 'open spotify' in query:
            speak('Opening spotify')
            webbrowser.open("spotify.com")
        elif 'open stack overflow' in query:
            speak('Opening stackoverflow')
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            speak('Playing music')
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is, {strTime}")
        elif "code" in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "send email to" in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = 'receiver@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent.')
            except Exception as e:
                speak("Sorry can't send")
        elif 'quit' in query:
            print('Thank you for using')
            exit()