robin1 = {
    "fullname": "Richard John Grayson",
    "name": "Dick Grayson",
    "short_name": "Grayson",
    "hero_name": "Nightwing",
    "tools": {
        "main_waepon": "escrima sticks", #weapon of choice
        "throwable": "wing-dings",
    },
    "skills_list": ["acrobatics", "stealth", "escapology", "hacking"],
    "skills" : "Nightwing's skills include acrobatics, stealth, escapology, hacking and more",
    "facts": {
        "01": "Nightwing is known to be the greatest acrobat in his universe",
    }
}

robin2 = {
    "fullname": "Jason Peter Todd",
    "name": "Jason",
    "short_name": "Jason",
    "hero_name": "Red Hood",
    "tools": {
        "main_waepon": "pistols", #weapon of choice
        "throwable": "grenades ",
    },
    "skills_lists": ["espionage", "disguise", "strategist", "weapon mastery"],
    "skills": "Red Hood's skills include espionage, disguise, strategist, weapon mastery and more",
    "facts": {
        "01": "After bathing in the Lazarus, Jason's body has enhanced strength, stamina and durability",
    }
}

robin3 = {
    "fullname": "Barbara Joan Gordon",
    "name": "Barbara",
    "short_name": "Babs",
    "hero_name": "Batgirl",
    "tools": {
        "main_waepon": "tonfas", #weapon of choice
        "throwable": "bat-a-rangs",
    },
    "skills_list": ["hacking", "acrobatics", "photographic memory", "informations expert"],
    "skills": "Batgirl's skills include hacking, acrobatics, a photographic memory, and is a informations expert",
    "facts": {
        "01": "Batgirl has control over Luthor's advanced satelites without his knowledge",
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
    "skills_list": ["espionage", "detective skills", "genius intellect", "hacking"],
    "skills": "Robin's skills include espionage, detective skills, genius intellect, and hacking",
    "facts": {
        "01": "Tim's detective skills rivals that of Batman himself",
    }
}

def all_info(robin, res):
    return robin[res]

def what_can(robin):
    robin["skills"] #need to list thru
    return robin["skills"]
    #print(robin["hero_name"])