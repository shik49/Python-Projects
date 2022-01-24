"""
Desktop Assistant JARVIS

This project is a hard coded desktop assistant named JArvis which does daily tasks like greetings, sending an email,
grab the definition  of a word from wikipedia, opening a website, play music, tell time, openin a software, telling the 
meaining of a word and so on.
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from PyDictionary import PyDictionary

engine = pyttsx3.init('sapi5')  # Engine instance using sapi5 driver for windows
voices = engine.getProperty('voices')   
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)   #sets the male windows assistant[David] voice as an assistant

def speak(audio):       # speak funcion will get a text as an argument and turn into voice
    engine.say(audio)
    engine.runAndWait()     # We can change the values such as volumes etc

def wishMe():       # greeting function
    hour = datetime.datetime.now().hour
    print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis, sir, please tell me how may I help you")

def takecommand():          # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source: # requires pyaudio module to receive voice instruction
        print("Listening...")
        r.pause_threshold = 1
        print('xxx')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print('xxx')
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in') # here google web speech API is used to recognize text from audio
        print(f"User said: {query}\n")  
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

'''
We'll use smtplib module to send the email over smtp port 587 which is the common one.
Plus access to less secure apps shold be enabled on google to send mail via gmail
'''

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shikharzxy@gmail.com', 'qwefghnm,')
    server.sendmail('shikharzxy@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak('harry is a good boy')
    wishMe()
    # while True:
    while True:
        query = takecommand().lower()
        # Executing tasks based on the query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))     # can make random song function too

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\shikh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe"
            os.startfile(codepath)

        elif 'email to shikhar' in query:
            try: 
                speak("What should I say?")
                content = takecommand()
                to = 'mail.shikharg@gmail.com'
                sendemail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'dictionary' in query:
            dict = PyDictionary()
            try:
                speak("please mention the word for its meaning")
                word = takecommand()
                meaning = dict.meaning(word)
                speak(meaning)
            except Exception as e:
                print(e)
                speak("Not able to open dictionary")

        elif 'quit' in query:
            exit()