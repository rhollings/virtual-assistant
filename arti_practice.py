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

# https://github.com/mmirthula02/AI-Personal-Voice-assistant-using-Python/blob/master/venv/virtual.py

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
speak("Loading your AI personal assistant")

wishMe()

if __name__=='__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Arti is shutting down,Good bye')
            print('your personal assistant Arti is shutting down,Good bye')
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
            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            speak('Here is the latest news')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'question' in statement:
            speak('I can answer computational and geographical questions, what question do you want to ask?')
            question=takeCommand()
            app_id="XP4G3A-XXR48W527Q"
            client = wolframalpha.Client(app_id) #USE OWN APP ID
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Arti version 1 point O, your virtual assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,tell time, search wikipedia, tell weather' 
                  'In different cities, get news and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Rod")
            print("I was built by Rod")

        elif "weather" in statement:
            api_key="56ca487c31152ebcada8f9c7ab0a4ef3" 
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"] - 273.15
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in celsius unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            #subprocess.call(["shutdown", "/l"])
			
time.sleep(3)