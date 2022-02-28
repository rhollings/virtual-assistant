import requests
import urllib.parse
import pandas as pd
from requests_html import HTML
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

  output = []
  
  for result in results:

    item = {
      'title': result.find(css_identifier_title, first=True).text,
      'link': result.find(css_identifier_link, first=True).attrs['href'],
      #'text': result.find(css_identifier_text, first=True).text
    }
    
    output.append(item)

  data = response.html.find(css_identifier_info)

  l = []

  for d in data:
    x = {
      'info': d.find(css_identifier_info, first=True).text
    }
    l.append(x)
        
  return l

def google_search(query):
  response = get_results(query)
  return parse_results(response)


#results = google_search('where is the eiffel tower')
#print(results)


def tell_joke():
  pass

def tell_peom():
  pass

def give_advice():
  pass