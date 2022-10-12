# Game releases: October 25 2022

# Dick Grayson // Nightwing
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
    "skills_list": ["acrobatic maneuvering", "stealth", "escapology", "hacking"],
    "skills" : "Nightwing's skills include acrobatics, stealth, escapology, hacking and more",
    "specialty": "Nightwing is a team player offering buffs and boosts to teammates all while having best maneuverability",
    "facts": {
        0: "Nightwing is known to be the greatest acrobat in his universe",
        1: "Grayson is Bruce's first robin, the original boy wonder since April 1940",
        2: "Grayson inherited billions from Alfred's untimely passing",
        3: "Grayson spent nights undercover in Arkham Asylum disguised as Joker",
        4: "Talon, also known as William Cobb is Grayson's great grandfather"
    }
}

# Jason Todd // Red Hood
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
    "specialty": "Red Hood specializes in range and grabs",
    "facts": {
        0: "After bathing in the Lazarus, Jason's body has enhanced strength, stamina and durability",
        1: "Bruce once found Jason stealing the tires from the batmobile",
        2: "As a teen, Jason would dress up as a member of the Red Hood Gang to rob stores for money"
    }
}

# Barbara Gordon // Batgirl
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
    "specialty": "Batgirl specializes in close quarter combat",
    "facts": {
        0: "Batgirl has control over Luthor's advanced satelites without his knowledge",
        1: "Barbara's father is James Gordon, the former Commissioner",
        2: "Barbara is the first of 3 batgirls"
    }
}

# Tim Drake // Robin
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
    "skills_list": ["stealth tech", "detective skills", "short range teleportation", "hacking"],
    "skills": "Robin's skills include espionage, detective skills, genius intellect, and hacking",
    "specialty": "Robin focuses on using stealth and gadets to disorientate enemies",
    "facts": {
        0: "Tim's detective skills rivals that of Batman himself",
        1: "Tim is the third male robin, after Dick and Jason",
        2: "Tim scored 100 percent on the SAT while still in middle school"
    }
}


# A current misson tracker??

# STATS include Power/Health/Armor/Melee+crit/Range+crit
# what are critical chances and damage? 

# What all characters can do vs individually  

from itertools import count
import random
import datetime


def all_info(robin, res):
    return robin[res]

def what_can(robin):
    robin["skills"] #need to list thru
    return robin["skills"]
    #print(robin["hero_name"]) for testing

def give_specialty(robin):
    robin["specialty"] #need to list thru
    return robin["specialty"]
    #print(robin["hero_name"]) for testing
print(give_specialty(robin1))

def move_set(robin):
    moves = robin["moves"]
    x = ', '.join(moves)
    return x
    #print(x)  for testings

def tell_fact(robin):
    x = len(robin["facts"]) #amount of facts on hero
    y = random.randint(0, x)
    return robin["facts"][y]
    #print(robin["facts"][y]) for testing

to_choose = (robin1, robin2, robin3, robin4)
def random_facts(): # needs work?
    x = random.choice(to_choose)
    print(x['name'])
    facts = x['facts']
    rand1 = random.choice(facts) #random.choice simplifies code
    return rand1

def gotham_knights(robin, command):
    if robin == 'grayson':
        if command == 'combat':
            return move_set(robin1)
        elif command == 'skills':
            return what_can(robin1)
        elif command == 'specialty':
            return give_specialty(robin1)
        elif command == 'fact':
            return tell_fact(robin1)
    elif robin == 'jason':
        if command == 'combat':
            return move_set(robin2)
        elif command == 'skills':
            return what_can(robin2)
        elif command == 'specialty':
            return give_specialty(robin2)
        elif command == 'fact':
            return tell_fact(robin2)
    elif robin == 'barbara':
        if command == 'combat':
            return move_set(robin3)
        elif command == 'skills':
            return what_can(robin3)
        elif command == 'specialty':
            return give_specialty(robin3)
        elif command == 'fact':
            return tell_fact(robin3)
    elif robin == 'tim':
        if command == 'combat':
            return move_set(robin4)
        elif command == 'skills':
            return what_can(robin4)
        elif command == 'specialty':
            return give_specialty(robin4)
        elif command == 'fact':
            return tell_fact(robin4)

    
    
def countdown_to_release():
    release_date = datetime.date(2022, 10, 21)
    today = datetime.date.today()
    if release_date <= today:
        return "The game has already released. Go play!!"
    res = abs(release_date - today)
    _str = 'The game releases in {} days'.format(res.days)
    return _str
