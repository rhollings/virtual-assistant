#function to record, print, update comics/manga currently reading
import sqlite3

conn = sqlite3.connect('ai_database.db')
c = conn.cursor()

'''
TABLE COLUMNS
book text,
chapter text,
character text,
company text,
finished text
'''
# to input many
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
    ('Fire Force', '0', 'Character', 'Studio', 'no'),
    ('Tokyo Revengers', '224', 'Character', 'Studio', 'no')
]

#c.execute("UPDATE comics SET chapter=:chapter WHERE book=:book", {"chapter": chapter, "book": book})

#c.execute("UPDATE manga SET character='Takemitchy' WHERE book='Tokyo Revengers'")

#c.executemany("INSERT INTO manga VALUES (?,?,?,?,?)", many_manga)

#c.execute("INSERT INTO manga VALUES ('Chainsaw Man', 'chapter', 'Denji', 'company', 'no') ")

#c.execute("DELETE FROM comics WHERE company='Studio'")

#c.execute("SELECT * FROM comics")
#print(c.fetchall())

#functions that update the tables
# Hey Arti, I'm reading _____ now. - 'Adding to list'
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

# Hey Arti, I'm on chpt __ for _____. - 'updating...'
# how to set finished default to 'no'
def update_current_read(type_of, book, chapter):
    if type_of == 'comic':
        c.execute("UPDATE comics SET chapter=:chapter WHERE book=:book", {"chapter": chapter, "book": book})
        print('comic')
    elif type_of == 'manga':
        c.execute("UPDATE manga SET chapter=:chapter WHERE book=:book", {"chapter": chapter, "book": book})
        print('manga')
    else:
        print('Something went wrong')

#update_current_read('manga', "Jujutsu Kaisen", '161')

def finised_book(type_of, book, finished):
    if type_of == 'comic':
        c.execute("UPDATE comics SET finihsed=:finished WHERE book=:book", {"finished": finished, "book": book})
        print('comic command updating')
    elif type_of == 'manga':
        c.execute("UPDATE manga SET finished=:finished WHERE book=:book", {"finished": finished, "book": book})
        print('manga command updating')
    else:
        print('Type Not Found')
    pass
#finised_book('manga', 'Chainsaw Man', 'yes')

# Show me all reads
# Show unfinished/finished reads
def print_current_reads(type_of):
    comics = c.execute("SELECT book FROM comics")
    all_comics = comics.fetchall()
    manga = c.execute("SELECT book FROM manga")
    all_manga = manga.fetchall()
    reads = []
    if type_of == 'comic':
        for i in all_comics:
            reads.append(i[0])
        #print(reads)
        return reads
    elif type_of == 'manga':
        for j in all_manga:
            reads.append(j[0])
        #print(reads)
        return reads
    else:
        for j in all_manga:
            reads.append(j[0])
        for i in all_comics:
            reads.append(i[0])
        #print(reads)
        return reads

print_current_reads('')


# COMMITS COMMAND
conn.commit()
# CLOSE CONNECTION
conn.close()