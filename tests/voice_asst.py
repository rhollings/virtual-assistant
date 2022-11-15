import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id) # English

rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-40)
engine.setProperty("rate", 190)


engine.say("Hello, I am an artificial intelligence. Nice to meet you")

engine.setProperty('voice', voices[3].id) # French
engine.say("Salut, je suis un A.I, enchantee")

#print("Bonjour, Je m'appelle Arti")


engine.runAndWait()