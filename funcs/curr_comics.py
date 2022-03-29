#function to record, print, update comics/manga currently reading
import sqlite3

conn = sqlite3.connect('ai_database.db')
c = conn.cursor()

#make the tables

#functions that update the tables
