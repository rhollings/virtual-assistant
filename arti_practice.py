import speech_recognition as sr 
import pyttsx3 
import datetime
import wikipedia
import webbrowser 
import os
import time
import subprocess
#from ecapture import ecapture as ec 
import wolframalpha 
import json
import requests
from funcs.anime_funcs import have_you_watched
from funcs.goth_knights import *
from funcs.misc_funcs import *
from funcs.movies import *

from dotenv import load_dotenv

from funcs.utils import affirm_speak

load_dotenv()
WEATHER_KEY = os.getenv('WEATHER_KEY')
WOLFRAMALPHA_KEY = os.getenv('WOLFRAMALPHA_KEY')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-55)
engine.setProperty('voice', voices[10].id) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    curr_hour = datetime.datetime.now().hour
    if curr_hour >= 5 and curr_hour < 12:
        speak("Good Morning User")
        print("Good Morning")
    elif curr_hour >= 12 and curr_hour < 18:
        speak("Good Afternoon User")
        print("Good Afternoon")
    elif curr_hour >= 18 and curr_hour < 23:
        speak("Good Evening User")
        print("Good Evening")
    else:
        speak("It is late User")
        print("It is late")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Pardon, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant")
speak("Loading ")

wishMe()

affirm = affirm_speak()

if __name__=='__main__':

    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "goodbye" in statement or "go to sleep" in statement or "stop" in statement or "take a break" in statement:
            speak('Arti is shutting down, Good bye')
            print('your virtual assistant Arti is shutting down,Good bye')
            break
        
        elif 'hi' in statement or 'hello' in statement or 'hey' in statement:
            speak('Hello, may I assist with something?')

        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)        

        elif 'open youtube' in statement:
            speak(affirm)
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            speak(affirm)
            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            speak('Here is the latest news')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'look up' in statement:
            speak(affirm)
            statement = statement.replace("look up", "")
            results = google_search(statement)
            to_speak = results[0]
            if to_speak == []:
                to_speak = results[1][0]['text']
            else:
                to_speak = to_speak[0]['info']
            speak(to_speak)

        elif 'mum joke' in statement: 
            joke = mama_joke()
            speak(joke)

        elif 'next' in statement and 'marvel' in statement:
            speak(affirm)
            res = next_mcu_title()
            text = res[0]
            image = res[1]
            speak(text)

        elif 'question' in statement:
            speak('I can answer computational and geographical questions, what question do you want to ask?')
            question=takeCommand()
            app_id = WOLFRAMALPHA_KEY
            client = wolframalpha.Client(app_id) #USE OWN APP ID
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'gotham knight' in statement:
            speak('Loading Gotham Knights video game logic, who do you need?')
            hero = takeCommand().lower()
            if 'no thanks' in hero:
                continue
            elif 'nightwing' in hero or 'grayson' in hero:
                speak('Hero chosen is Nightwing')
                help = takeCommand().lower()
                if 'something' in help:
                    fact = tell_fact(robin1)
                    speak(fact)
                elif 'information' in help:
                    x = takeCommand().lower()
                    info = all_info(robin1, x)
                    speak(info)
                elif 'never mind':
                    continue
            elif 'red hood' in hero or 'jason' in hero:
                speak('Hero chosen is Red Hood')
                help = takeCommand().lower()
                if 'something' in help:
                    fact = tell_fact(robin2)
                    speak(fact)
                elif 'information' in help:
                    x = takeCommand().lower()
                    info = all_info(robin2, x)
                    speak(info)
                elif 'never mind':
                    continue
            elif 'batgirl' in hero or 'barbara' in hero:
                speak('Hero chosen is Batgirl')
                help = takeCommand().lower()
                if 'something' in help:
                    fact = tell_fact(robin3)
                    speak(fact)
                elif 'information' in help:
                    x = takeCommand().lower()
                    info = all_info(robin3, x)
                    speak(info)
                elif 'never mind':
                    continue
            elif 'robin' in hero or 'tim' in hero:
                speak('Hero chosen is Robin')
                help = takeCommand().lower()
                if 'something' in help:
                    fact = tell_fact(robin4)
                    speak(fact)
                elif 'information' in help:
                    x = takeCommand().lower()
                    info = all_info(robin4, x)
                    speak(info)
                elif 'never mind':
                    continue

        elif 'recommend' in statement and 'anime' in statement:
            speak(affirm)
            anime = have_you_watched()
            speak("Have you seen " + anime + " ?")


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Arti version 1 point O, your virtual assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,tell time, search wikipedia, tell weather' 
                  'In different cities, get news and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was created by Rod")
            print("I was created by Rod")

        elif "rod" in statement or "pj" in statement:
            speak("PJ is a genuis, the man you speak of is my creator.")

        elif 'cecile' in statement or 'boo boo' in statement:
            speak('meanie pants, i mean, she is a beautiful french lady married to rod')

        elif 'movies' in statement:
            speak(affirm)
            x = get_trending_movies()
            speak(x)
        
        elif "weather" in statement:
            api_key = WEATHER_KEY 
            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+city_name+"&units=metric"+"&appid="+api_key
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                temp_min = y["temp_min"]
                temp_max = y ["temp_max"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in celsius is " +
                      str(current_temperature) +
                      "\n with a low of " +
                      str(temp_min) +
                      "\n and a high of " +
                      str(temp_max) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(current_temperature) +
                      "\n Lowest = " +
                      str(temp_min) +
                      "\n Highest = " +
                      str(temp_max) +
                      "\n description = " +
                      str(weather_description))
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            #subprocess.call(["shutdown", "/l"])
			
time.sleep(3)