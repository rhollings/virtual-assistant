#function to record, print, update comics/manga currently reading
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

#c.executemany("INSERT INTO comics VALUES (?,?,?,?,?)", many_comics)

#c.execute("INSERT INTO comics VALUES ('book', 'chapter', 'character', 'company', 'yes or no') ")

#c.execute("SELECT * FROM comics")
#print(c.fetchall())

#functions that update the tables
def add_read(book, chapter, character, company):
    c.execute("SELECT * FROM comic")
    print(book, chapter, character, company)

add_read('Book', 'Chapter', 'Character', 'Company')

def update_current_read(book, chapter, finished):
    pass

def print_current_reads():
    pass


# COMMITS COMMAND
conn.commit()

# CLOSE CONNECTION
conn.close()

print('Script ran succesfully')
