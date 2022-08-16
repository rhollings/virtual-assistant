import requests

response = requests.get("https://my-superher0-api.herokuapp.com/data")
results = response.json()
data = results


# How to search via JSON ?? 
# return nightwing

def search_hero(name):
    for i in data:
        hero_name = i["name"]
        if hero_name.lower() == name:
            return i
    return 'Not Found'

print(search_hero('nightwing'))

# sentence = name aka real_name, race gender, side
# Nightwing also known as Dick Grayson, Human Male, Hero