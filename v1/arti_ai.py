# IMPORTS 
import sys
sys.path.insert(0, '/Users/rod/Code/Python3/virtual-assistant/funcs')


import speech_recognition as sr 
import pyttsx3 
import datetime
import time
import wikipedia
import webbrowser 
import os
#import subprocess
#from ecapture import ecapture as ec 
from wolfram import *
#import json
import requests
from anime_comics import print_current_reads
from anime_funcs import have_you_watched
from goth_knights import *
from misc_funcs import *
from movies import *
from utils import *
from dotenv import load_dotenv

# How to import modules ???

load_dotenv() # initiates .env file
WEATHER_KEY = os.getenv('WEATHER_KEY')
WOLFRAMALPHA_KEY = os.getenv('WOLFRAMALPHA_KEY')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
engine.setProperty('voice', voices[7].id) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    curr_hour = datetime.datetime.now().hour
    if curr_hour >= 5 and curr_hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif curr_hour >= 12 and curr_hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")
    elif curr_hour >= 18 and curr_hour < 23:
        speak("Good Evening")
        print("Good Evening")
    else:
        speak("It is late")
        print("It is late")

to_repeat = repeat_speak()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            #speak("Pardon, please say that again")
            speak("Sorry ")
            speak(to_repeat)
            return "None"
        return statement

print("Loading your AI personal assistant")
speak("Loading ")

wishMe()

affirm = affirm_speak()
closing = closing_speak()

# wait for input ex. "Hey Bot"
# convo tracking or reminders with SQL?? 


speak("How can I help you?")
if __name__=='__main__':

    while True:
        #speak("How can I help you?")
        print("Awaiting command...")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "goodbye" in statement or "go to sleep" in statement or "stop" in statement or "take a break" in statement:
            #speak('Arti is shutting down, Good bye')
            speak(closing)
            print('your virtual assistant Arti is shutting down, Good bye')
            break
        
        elif 'hi' in statement or 'hello' in statement or 'hey' in statement:
            speak('Hello, may I assist with something?')

        # talk_to_me func - arti speaks thru assortment of items
        # like reminders, news, etc.

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

        elif 'chat' in statement:
            # implement while loop to have conversation
            speak(affirm)
            x = 'some_chat_function'
            speak(x)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'look up' in statement:
            speak(affirm)
            statement = statement.replace("look up", "")
            webbrowser.open_new_tab(statement)
            results = google_search(statement)
            to_speak = results[0]
            if to_speak == []:
                to_speak = results[1][0]['text']
            else:
                to_speak = to_speak[0]['info']
            speak(to_speak)
            time.sleep(5)

        elif 'mama joke' in statement: 
            joke = mama_joke()
            speak(joke)

        elif 'dark joke' in statement:
            joke = dark_joke()
            x, y = joke[0], joke[1]
            speak(x)
            time.sleep(2)
            speak(y)

        elif 'next' in statement and 'marvel' in statement:
            speak(affirm)
            res = next_mcu_title()
            text = res[0]
            image = res[1]
            webbrowser.open_new_tab(image)
            speak(text)
            time.sleep(5)

        elif 'flip a coin' in statement:
            speak('flipping a coin')
            to_say = coin_flip()
            speak(to_say)
            time.sleep(5)

        elif 'choose' in statement:
            speak('what are your options')
            options = takeCommand()
            to_say = choose_for_me(options)
            speak(to_say)

        elif 'google this' in statement: # reconfig
            speak('what question do you want to ask?')
            question=takeCommand()
            answer = to_respond(question)
            speak(answer)
            print(answer)
            time.sleep(5)

        # USE Wolfram API
        elif 'question' in statement:
            speak('what is your question ?')
            question = takeCommand()
            answer = to_respond(question)
            speak(answer)
            time.sleep(5)

        elif 'gotham knight' in statement:
            speak('Loading Gotham Knights video game logic, who do you need?')
            while True:
                new_statement = takeCommand().lower()
                if "stop" in new_statement or "thanks" in new_statement:
                    break
                elif 'grayson' in new_statement:
                    hero = new_statement.split(" ")
                    results = gotham_knights(hero[0], hero[1])
                    speak(results)
                elif 'jason' in new_statement:
                    hero = new_statement.split(" ")
                    results = gotham_knights(hero[0], hero[1])
                    speak(results)
                elif 'barbara' in new_statement:
                    hero = new_statement.split(" ")
                    results = gotham_knights(hero[0], hero[1])
                    speak(results)
                elif 'tim' in new_statement:
                    hero = new_statement.split(" ")
                    results = gotham_knights(hero[0], hero[1])
                    speak(results)
                elif 'come out' in new_statement or 'release' in new_statement:
                    results = countdown_to_release()
                    speak(results)
                elif 'random' in new_statement or 'fact' in new_statement:
                    results = random_facts()
                    speak(results)
            time.sleep(5)

        elif 'open' in statement and 'reading' in statement:
            speak('Inside comic/anime database')
            while True:
                new_statement = takeCommand().lower()
                if "stop" in new_statement or "thanks" in new_statement:
                    break
                elif "update" in new_statement:
                    speak('what book would you like to update?')
                elif "what am i reading" in new_statement:
                    speak('comics or manga?')
                    while True:
                        thrd_statement = takeCommand().lower()
                        if 'comic' in thrd_statement:
                            arr = print_current_reads('comic')
                            for i in arr:   
                                speak(i)
                            break
                        elif 'manga' in thrd_statement:
                            arr = print_current_reads('manga')
                            for i in arr:   
                                speak(i)
                            break
                        elif 'both' in thrd_statement:
                            arr = print_current_reads('')
                            for i in arr:   
                                speak(i)
                            break
                        else:
                            speak('Exiting, Try again')
                            break
                # 'give read' 'say read' 'return reads' ??
            time.sleep(5)

        elif 'recommend' in statement and 'anime' in statement:
            speak(affirm)
            anime = have_you_watched()
            speak("Have you seen " + anime + " ?")
            print(anime)
            time.sleep(5)
        
        elif 'fact' in statement and 'anime' in statement:
            speak(affirm)
            anime = tell_fact()
            speak("Did you know that: " + anime)
            print("Did you know that: " + anime)
            time.sleep(5)


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Arti, version 1 point O, a virtual assistant. I am programmed to do minor tasks like '
                  'searching the web, tell time, weather in different cities, recommend an anime, tell jokes, ' 
                  'get news and answer computational or geographical questions too!')
            time.sleep(5)


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was created by PJ")
            time.sleep(3)

        elif "rod" in statement or "pj" in statement:
            speak("PJ is a genuis, the man you speak of is my creator.")
            time.sleep(3)

        elif 'cecile' in statement or 'boo boo' in statement:
            speak('meanie pants, i mean, she is a beautiful french lady married to rod')
            time.sleep(5)

        elif 'introduction' in statement or 'introduce' in statement:
            speak('Hello, I am an A.I. created by Rod. I do not yet have a name.')
            time.sleep(5)

        elif 'movies' in statement:
            speak(affirm)
            x = get_trending_movies()
            speak(x)
            time.sleep(5)
        
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
            time.sleep(5)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            #subprocess.call(["shutdown", "/l"])
			
time.sleep(3)