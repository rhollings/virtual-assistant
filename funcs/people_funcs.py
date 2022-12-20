from calendar import month
import datetime
from utils import month_texts, day_texts


# Format dates for function
# Test cases: '21st of June', 'March 3rd', 'November the 19th'
# How to format different types of input ??
def format_date(input_date):
    pass


# Q: When is my birthday?
# DateTime Format 2022-10-18 23:45:03.366769 
def return_birthday(month, day, year):
    bd = datetime.date(year, month, day)
    today = datetime.date.today()
    res = bd - today
    
    _str = 'Your birthday is in {} days'.format(res.days)
    return _str

#print(return_birthday(10, 5, 2022))

#current_date = datetime.datetime(10, 5, 2022)

#print(int(current_date.strftime("%d")))