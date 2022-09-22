import datetime

# Q: When is my birthday?
def return_birthday(date_given):
    bd = date_given
    today = datetime.date.today()
    res = abs(bd - today)
    _str = 'Your birthday is in {} days'.format(res.days)
    return _str

