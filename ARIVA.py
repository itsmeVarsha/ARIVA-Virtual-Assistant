import re
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time 
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import random
import shutil
from urllib.request import urlopen


print("Loading    Ariva")  
print("your AI personal Assistant")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("Welcome", uname.center(columns))
     
    speak("How can i Help you ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading    Ariva")  
speak(" your AI personal Assistant")
wishMe()

if __name__=='__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement=takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant is shutting down, Good Bye')
            print('your personal assistant is shutting down, Good Bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement=statement.replace("wikipedia", "")
            results=wikipedia.summary(statement,sentences=3)
            speak("According to Wikipedia")

            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("http://www.youtube.com")
            speak("Youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("http://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail opens now")
            time.sleep(5)

        elif 'weather' in statement:
            api_key="f065fa6fafdc01beaca9a98f5f3b9335"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name ")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response=requests.get(complete_url)
            x=response.json()
            if x["cod"] != "404":
                y=x["main"]
                current_temperature=y["temp"]
                current_humidity=y["humidity"]
                z=x["weather"]
                weather_description=z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n Humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n Description = " +
                      str(weather_description))

            else:
                speak("City not Found")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'date' in statement:
            dt_string=datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"the date is {dt_string}")
            print(f"the date is {dt_string}")

        elif 'what can you do' in statement or 'Who are you' in statement:
            speak(' Hii,I am ARIVA   version 1 point 0 your personal assisytance. I am programmed to perform minor tasks like'
            'opening youtube, google chrome, gmail and stackoverflow ,predict time take a phot, search wikipedia, predict weather'
            'in different cities , get top headline news from Times  of India' 
            'you cane ask me computational or geographical qoestion too !!')
            print(' Hii,I am ARIVA   version 1 point 0 your personal assisytance. I am programmed to perform minor tasks like'
            'opening youtube, google chrome, gmail and stackoverflow ,predict time take a phot, search wikipedia, predict weather'
            'in different cities , get top headline news from Times  of India' 
            'you cane ask me computational or geographical qoestion too !!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Team Technofy")
            print("I was built by Team Technofy")

        elif "stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/?from=mdr")
            speak('Here are some headlines from the Times of India,Happy reading')
            print('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'python playlist' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=aqvDTCpNRek&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
            speak("Here is the playlist for Python. Hope you have a great learning !!")
            print("Here is the playlist for Python. Hope you have a great learning !!")

        elif 'play music' in statement or "play song" in statement:
            speak("Here you go with music")
            print("Here you go with music")
            music_dir = "G:\\songs\\"
            songs = os.listdir(music_dir)
            print(songs)   
            d=random.choice(songs)
            os.startfile('G:\\songs\\'+d)
            time.sleep(5)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement=statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'love fact' in statement:
            speak("who is he or she")
            uname = takeCommand()
            speak("Welcome ")
            speak(uname)
            columns = shutil.get_terminal_size().columns
            speak("It is 7th sense that destroy all other senses and your life so don't love.")
            print("It is 7th sense that destroy all other senses and your life so don't love.")

        elif 'reason behind you' in statement:
            speak("I am created for helping you in Handsfree actions")
            speak("I am created for helping you in Handsfree actions")

        # elif "write a note" in statement:
        #     speak("What should i write, sir")
        #     note = takeCommand()
        #     file = open('ARIVA.txt', 'w')
        #     speak("Sir, Should i include date and time")
        #     snfm = takeCommand()
        #     if 'yes' in snfm or 'sure' in snfm:
        #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #         file.write(strTime)
        #         file.write(" :- ")
        #         file.write(note)
        #     else:
        #         file.write(note)
         
        # elif "Display note" in statement:
        #     speak("Showing Notes")
        #     file = open("ARIVA.txt","r")
        #     print(file.read())
        #     speak(file.read(6))

        elif 'answer me' in statement:
            speak('I can answer to compitational and geographical questions. Do you have any question to ask')
            print('I can answer to compitational and geographical questions. Do you have any question to ask')
            question = takeCommand()
            app_id= "HT88T5-K47XT55R32"
            client=wolframalpha.Client('HT88T5-K47XT55R32')
            res=client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'covid report' in statement:
            speak("here is your covid report")
            print("here is your covid report")
            webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")

        elif "log off" in statement or "sign out" in statement:
            speak("Okay , Your pc will log out in 10 second. Make  sure you exit from all the applications")
            print("Okay , Your pc will log out in 10 second. Make  sure you exit from all the applications")
            subprocess.call(["shutdown","/l"])

        elif 'where is' in statement:
            print('..')
            words = statement.split('where is')
            print(words[-1])
            link = str(words[-1])
            link = re.sub(' ', '', link)
            engine.say('Locating')
            engine.say(link)
            engine.runAndWait()
            link = f'https://www.google.co.in/maps/place/{link}'
            print(link)
            webbrowser.open(link)
        
        elif 'location' in statement:
            speak("you are in")
            url='http://ipinfo.io/json'
            response=urlopen(url)
            data= json.load(response)
            speak(data)
            print(data)

        
time.sleep(3)