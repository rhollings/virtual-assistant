import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
#engine.say("I will speak this text hello bye bye this that")

engine.say("Bonjour, Je m'appelle Arti")
print("Bonjour, Je m'appelle Arti")

#pyttsx3 does not speak other languages


engine.runAndWait()
'''
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1
'''