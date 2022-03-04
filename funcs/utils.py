import random

opening_text = [
    "I'm on it",
    "Okay, I'm working on it",
    "Just a second",
    "One second",
    "Just a moment",
    "Processing",
    "Loading...",
    "Understood",
    "Right away",
    "Will do",
]

closing_text = [
    "See you later boss",
    "Taking a break",
    "I'm here if you need me",
    "Wake me if you need me",
    "Staying close by",
    "Later boss",
    "Later",
]

month_texts = {
    "01": "January",
    "02": "Feburary",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

day_texts = {
    "01": "1st",
    "02": "2nd",
    "03": "3rd",
    "04": "4th",
    "05": "5th",
    "06": "6th",
    "07": "7th",
    "08": "8th",
    "09": "9th",
    "10": "10th",
    "11": "11th",
    "12": "12th",
    "13": "13th",
    "14": "14th",
    "15": "15th",
    "16": "16th",
    "17": "17th",
    "18": "18th",
    "19": "19th",
    "20": "20th",
    "21": "21st",
    "22": "22nd",
    "23": "23rd",
    "24": "24th",
    "25": "25th",
    "26": "26th",
    "27": "27th",
    "28": "28th",
    "29": "29th",
    "30": "30th",
    "31": "31st",
}

def affirm_speak():
    x = len(opening_text)
    y = random.randint(0, x-1)
    return opening_text[y]
    #print(opening_text[y])

def closing_speak():
    x = len(closing_text)
    y = random.randint(0, x-1)
    return closing_text[y]


# A better way to tell days

def tell_date(date_given):
    x = date_given.split("-")
    this_day = x[2]
    day = day_texts[this_day]
    this_month = x[1]
    month = month_texts[this_month]
    this_year = x[0]
    year = this_year
    # DAY of MONTH in YEAR
    res = day + " of " + month + " in " + year
    #print(res)
    return res

#tell_date("2022-03-02")