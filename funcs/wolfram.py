# https://products.wolframalpha.com/api/documentation/#top 

import requests
import os
from dotenv import load_dotenv

load_dotenv()
WOLFRAMALPHA_KEY = os.getenv('WOLFRAMALPHA_KEY')

def to_respond(question):
    wolf_url = 'http://api.wolframalpha.com/v2/query'
    app_id_url = '?appid='+str(WOLFRAMALPHA_KEY)+'&input='
    end_url = '&output=json'
    res = question.replace(" ", "%20")
    url = wolf_url + app_id_url + res + end_url

    to_fetch = requests.get(url)
    results = to_fetch.json()
    data = results['queryresult']['pods'][1]['subpods'][0]
    
    return data['plaintext']

# Ex. print(to_respond('who is the president of the united states'))