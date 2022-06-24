# Game releases: October 25 2022

robin1 = {
    "fullname": "Richard John Grayson",
    "name": "Dick Grayson",
    "short_name": "Grayson",
    "hero_name": "Nightwing",
    "tools": {
        "main_waepon": "escrima sticks", #weapon of choice
        "throwable": "wing-dings",
    },
    "moves": ["punching", "kicking", "and sticks"],
    "skills_list": ["acrobatics", "stealth", "escapology", "hacking"],
    "skills" : "Nightwing's skills include acrobatics, stealth, escapology, hacking and more",
    "facts": {
        0: "Nightwing is known to be the greatest acrobat in his universe",
        1: "Grayson is Bruce's first robin, the original boy wonder",
        2: "Nightwing is currently the richest memeber of the family"
    }
}

robin2 = {
    "fullname": "Jason Peter Todd",
    "name": "Jason Todd",
    "short_name": "Jason",
    "hero_name": "Red Hood",
    "tools": {
        "main_waepon": "pistols", #weapon of choice
        "throwable": "grenades ",
    },
    "moves": ["punching", "kicking", "and shooting"],
    "skills_list": ["espionage", "disguise", "strategist", "weapon mastery"],
    "skills": "Red Hood's skills include espionage, disguise, strategist, weapon mastery and more",
    "facts": {
        0: "After bathing in the Lazarus, Jason's body has enhanced strength, stamina and durability",
        1: "Bruce once found Jason stealing the tires from the batmobile"
    }
}

robin3 = {
    "fullname": "Barbara Joan Gordon",
    "name": "Barbara Gordon",
    "short_name": "Babs",
    "hero_name": "Batgirl",
    "tools": {
        "main_waepon": "tonfas", #weapon of choice
        "throwable": "bat-a-rangs",
    },
    "moves": ["punching", "kicking", "and sticks"],
    "skills_list": ["hacking", "acrobatics", "photographic memory", "informations expert"],
    "skills": "Batgirl's skills include hacking, acrobatics, a photographic memory, and is a informations expert",
    "facts": {
        0: "Batgirl has control over Luthor's advanced satelites without his knowledge",
        1: "Barbara's father is James Gordon, the Commissioner"
    }
}

robin4 = {
    "fullname": "Timothy Jackson Drake",
    "name": "Tim Drake",
    "short_name": "Tim",
    "hero_name": "Robin",
    "tools": {
        "main_waepon": "bo-staff", #weapon of choice
        "throwable": "bat-a-rangs ",
    },
    "moves": ["punching", "kicking", "and sticks"],
    "skills_list": ["espionage", "detective skills", "genius intellect", "hacking"],
    "skills": "Robin's skills include espionage, detective skills, genius intellect, and hacking",
    "facts": {
        0: "Tim's detective skills rivals that of Batman himself",
        1: "Tim is the third male robin, after Dick and Jason"
    }
}


# A current misson tracker??

# STATS include Power/Health/Armor/Melee+crit/Range+crit
# what are critical chances and damage? 

# What all characters can do vs individually  

import random
import datetime


def all_info(robin, res):
    return robin[res]

def what_can(robin):
    robin["skills"] #need to list thru
    return robin["skills"]
    #print(robin["hero_name"]) for testing

def move_set(robin):
    moves = robin["moves"]
    x = ', '.join(moves)
    return x

def tell_fact(robin):
    x = len(robin["facts"]) #amount of facts on hero
    y = random.randint(0, x)
    return robin["facts"][y]
    #print(robin["facts"][y]) for testing

def gotham_knights(robin, command):
    if robin == 'grayson':
        if command == 'combat':
            return move_set(robin1)
        elif command == 'skills':
            return what_can(robin1)
        elif command == 'fact':
            return tell_fact(robin1)
    elif robin == 'jason':
        if command == 'combat':
            return move_set(robin2)
        elif command == 'skills':
            return what_can(robin2)
    elif robin == 'barbara':
        if command == 'combat':
            return move_set(robin3)
        elif command == 'skills':
            return what_can(robin3)
    elif robin == 'tim':
        if command == 'combat':
            return move_set(robin4)
        elif command == 'skills':
            return what_can(robin4)

to_choose = (robin1, robin2, robin3, robin4)
def random_hints(): # needs work?
    x = random.randint(0,4)
    y = to_choose[x]
    print(y['name'])
    values = y.values()
    print(values)
    
    
def countdown_to_release():
    release_date = datetime.date(2022, 10, 25)
    today = datetime.date.today()
    return release_date - today

print(countdown_to_release())