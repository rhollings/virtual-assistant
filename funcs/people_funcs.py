from calendar import month
import datetime
from utils import month_texts, day_texts


# Format dates for function
# Test cases: '21st of June', 'March 3rd', 'November the 19th'
# How to format different types of input ??
def format_date(input_date):
    pass


# Q: When is my birthday?
def return_birthday(date_given):
    bd = date_given
    today = datetime.date.today()
    res = abs(bd - today)
    _str = 'Your birthday is in {} days'.format(res.days)
    return _str

