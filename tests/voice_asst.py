import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
#engine.say("I will speak this text hello bye bye this that")

engine.say("Fetching database, one moment")
#print("Bonjour, Je m'appelle Arti")

#pyttsx3 does not speak other languages

# num7 male good
# num 10 good female

engine.runAndWait()
'''
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1
'''