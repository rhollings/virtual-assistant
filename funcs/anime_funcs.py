import random

anime_list = [
    'bleach',
    'black clover',
    'dragon ball',
    'jujutsu kaisen',
    'fma brotherhood',
    'naruto',
    'gintama',
    'one piece',
    'demon slayer',
    'attack on titan',
    'hunter x hunter',
    'boku no hero academia',
    'tokyo ghoul',
    ]
    

def have_you_watched():
    x = len(anime_list)
    y = random.randint(0, x)
    anime = anime_list[y]
    return anime

def tell_fact():
    pass

