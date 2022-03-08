from urllib import response
import requests
import urllib.parse
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import datetime
from funcs.utils import tell_date

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
  return parse_results(response)


#results = google_search('where is paris')
#print(results)
#print(type(results))


def mama_joke():
  response = requests.get("https://yomomma-api.herokuapp.com/jokes")
  joke = response.json()
  return joke["joke"]

def tell_joke():
  response = requests.get("") # https://humorapi.com/docs/#Random-Joke ??
  joke = response.json()
  return joke

def next_mcu_title(): # https://www.whenisthenextmcufilm.com/api?date=2022-03-01
  url_date_date = datetime.date.today().strftime("%Y:%m:%d")
  url_date = url_date_date.replace(":", "-")
  url = "https://www.whenisthenextmcufilm.com/api?date=" + url_date
  response = requests.get(url)
  result = response.json()
  x, res = '', []
  movie_poster = result["poster_url"]
  release_date = result["release_date"]
  title = result["title"]
  film_show = result["type"]
  date_x = tell_date(release_date)
  x = 'The next MCU ' + film_show + ', will be ' + title + ' and is set to release on the ' + date_x
  res = [x, movie_poster]
  return res
  #print(type(date))
  #print(res)


def tell_peom():
  pass

def tell_riddle():
  pass

def give_advice():
  pass