import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

create = """CREATE TABLE beatles (
                'fname' text,
                'lname' text,
                'nickname' text
            )"""

cursor.execute(create)

members = [
    ("john", "lennon", "the smart one"),
    ("paul", "mccartney", "the cute one"),
    ("george", "harrison", "the funny one"),
    ("ringo", "starr", "the quiet one")
]

insert = "INSERT INTO beatles VALUES (?, ?, ?)"

for member in members:
    cursor.execute(insert, member)

select = "SELECT fname, lname, nickname FROM beatles"
cursor.execute(select)

results = cursor.fetchall()
cursor.close()
connection.close()

print(results)