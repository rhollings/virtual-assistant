#from urllib import response // currently not using
from asyncio import run_coroutine_threadsafe
import random
import re
from tkinter import E
import requests
import urllib.parse
import pandas as pd
#from requests_html import HTML // currently not using
from requests_html import HTMLSession


def get_source(url):
  """Return the source code for the provided URL. 

  Args: 
      url (string): URL of the page to scrape.

  Returns:
      response (object): HTTP response object from requests_html. 
  """

  try:
      session = HTMLSession()
      response = session.get(url)
      return response

  except requests.exceptions.RequestException as e:
      print(e)

def scrape_google(query):

  query = urllib.parse.quote_plus(query)
  response = get_source("https://www.google.com/search?q=" + query)

  links = list(response.html.absolute_links)
  google_domains = ('https://www.google.', 
                    'https://google.', 
                    'https://webcache.googleusercontent.', 
                    'http://webcache.googleusercontent.', 
                    'https://policies.google.',
                    'https://support.google.',
                    'https://maps.google.')

  for url in links[:]:
      if url.startswith(google_domains):
          links.remove(url)

  return links

def get_results(query):
  
  query = urllib.parse.quote_plus(query)
  response = get_source("https://www.google.com/search?q=" + query + "&hl=en")
  
  return response

def parse_results(response):
  
  css_identifier_info = ".kno-rdesc" #.hgKElc
  css_identifier_result = ".tF2Cxc" #.tF2Cxc
  css_identifier_title = "h3" #h3
  css_identifier_link = ".yuRUbf a" #.yuRUbf a
  css_identifier_text = ".IsZvec span" #.IsZvec span
  
  results = response.html.find(css_identifier_result)[:1]

  search_res = []

  output = []
  
  for result in results:

    item = {
      'title': result.find(css_identifier_title, first=True).text,
      'link': result.find(css_identifier_link, first=True).attrs['href'],
      #'text': result.find(css_identifier_text, first=True).text
    }

    if result.find(css_identifier_text):
      item['text'] = result.find(css_identifier_text, first=True).text
    else:
      return None
    
    output.append(item)

  data = response.html.find(css_identifier_info)

  l = []

  for d in data:
    x = {
      'info': d.find(css_identifier_info, first=True).text
    }
    l.append(x)

  search_res.append(l)
  search_res.append(output)
        
  return search_res

def google_search(query):
  response = get_results(query)
  if parse_results(response) == None:
    return "Nothing found, try another way"
  else:
    return parse_results(response)


results = google_search('where is paris located')
print(results)
#print(type(results))


def mama_joke():
  # API DOCs = https://github.com/beanboi7/yomomma-apiv2 
  response = requests.get("https://yomomma-api.herokuapp.com/jokes")
  joke = response.json()
  return joke["joke"]

def tell_joke():
  response = requests.get("") # https://humorapi.com/docs/#Random-Joke ??
  joke = response.json()
  return joke

def dark_joke():
  url = 'https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw' #https://sv443.net/jokeapi/v2/
  response = requests.get(url)
  res = response.json()
  part1, part2 = res['setup'], res['delivery']
  x = []
  joke = (part1, part2)
  setup, line = joke[0], joke[1]
  x.append(setup)
  x.append(line)
  return x

#print(dark_joke())

# Need API's 
def tell_peom(): 
  # res = API output 
  pass

def tell_riddle():
  pass

def give_advice():
  pass

def coin_flip():
  coin = ['Heads', 'Tails']
  res = coin[random.randint(0, 1)]
  return res

# roll dice option <-- 
# dice have six sides // 1 out of 6 chance per side
def roll_dice():
  pass

def choose_for_me(choices):
  choices = choices.split()
  choice = choices[random.randint(0, len(choices)-1)]
  return choice

# double words split w/ split -- split by word 'or' ??
# if 'or' is added, must filter out 