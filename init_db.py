
import sqlite3

connection = sqlite3.connect('userDB.db')

with open('userSchema.sql') as f:
    connection.executescript(f.read())

#with open('userReadSchema.sql') as f:
#    connection.executescript(f.read())

#with open('bookSchema.sql') as f:
#    connection.executescript(f.read())
    
#with open('wanttoReasSchema.sql') as f:
#    connection.executescript(f.read())
    
with open('testSchema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()