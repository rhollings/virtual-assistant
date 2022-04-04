#function to record, print, update comics/manga currently reading
from re import X
import sqlite3

conn = sqlite3.connect('ai_database.db')
c = conn.cursor()

#make the tables
'''
c.execute("""CREATE TABLE manga ( 
        book text,
        chapter text,
        character text,
        company text,
        finished text
    )""")
'''
many_comics = [
    ('Nightwing', 'chapter', 'Nightwing', 'DC Comics', 'no'),
    ("World's Finest", 'chapter', 'Batman and Superman', 'DC Comics', 'no'),
    ('Fear State', 'chapter', 'Batman', 'DC Comics', 'no'),
    ('Justice League', 'chapter', 'Justice League', 'DC Comics', 'no')
]

many_manga = [
    ('My Hero Academia', '342', 'Character', 'Studio', 'no'),
    ('God of Highschool', 'chapter', 'Character', 'Studio', 'no'),
    ('Jujutsu Kaisen', '153', 'Character', 'Studio', 'no'),
    ('Fire Force', '0', 'Character', 'Studio', 'no')
    ('Tokyo Revengers', '224', 'Character', 'Studio', 'no')
]

#NEED TO UPDATE

#c.executemany("INSERT INTO comics VALUES (?,?,?,?,?)", many_comics)

#c.execute("INSERT INTO comics VALUES ('book', 'chapter', 'character', 'company', 'yes or no') ")

#c.execute("SELECT * FROM comics")
#print(c.fetchall())

#functions that update the tables
def add_read(type_of, book, chapter, character, company):
    x = 'Book is already in database'
    y = 'Adding', book, 'to db'
    if type_of == 'comic':
        print('comics')
        c.execute("SELECT * FROM comics WHERE book=:name", {"name": book})
    else:
        print('manga') 
        c.execute("SELECT * FROM manga WHERE book=:name", {"name": book})
    

    books = c.fetchall()
    if len(books) == 0:
        new_comic = (book, chapter, character, company, 'no')
        print(y)
        #c.executemany("INSERT INTO comics VALUES (?,?,?,?,?)", new_comic)
        print(new_comic)

    else:
        print(x)    
#add_read('comic', 'Batman', 'Chapter', 'Character', 'Company')


def update_current_read(type_of, book, chapter, finished):
    if type_of == 'comic':
        print('comic')
    else:
        print('manga')


def print_current_reads():
    #select both tables, return all titles 
    pass




# COMMITS COMMAND
conn.commit()
# CLOSE CONNECTION
conn.close()