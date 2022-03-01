from importlib.resources import open_text
import random

opening_text = [
    "I'm on it",
    "Okay, I'm working on it",
    "Just a second",
    "One second",
    "Just a moment",
    "Processing",
    'Loading...',
]

def affirm_speak():
    x = len(opening_text)
    y = random.randint(0, x-1)
    return opening_text[y]
    #print(opening_text[y])