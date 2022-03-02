import random
import requests

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

anime_names = [
    'bleach',
    'black_clover',
    'dragon_ball',
    'jujutsu_kaisen',
    'fma_brotherhood',
    'naruto',
    'gintama',
    'itachi_uchiha',
    'one_piece',
    'demon_slayer',
    'attack_on_titan',
    'hunter_x_hunter',
    'boku_no_hero_academia',
]
    

def have_you_watched():
    x = len(anime_list)
    y = random.randint(0, x-1)
    anime = anime_list[y]
    return anime

def tell_fact():
    x = len(anime_names)
    y = random.randint(0, x-1)
    anime = anime_names[y]
    to_fetch = 'https://anime-facts-rest-api.herokuapp.com/api/v1/'
    url = to_fetch + anime
    response = requests.get(url)
    results = response.json()
    a = results['total_facts']
    b = random.randint(0 , a-1)
    facts = results['data']
    fact = facts[b]
    res = fact['fact']
    print(res)