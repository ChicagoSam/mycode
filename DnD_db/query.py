# WORK IN PROGRESS, HARDCODEQUERY.PY HOLDS WORKING QUERY AT THIS POINT IN TIME

import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()

c.execute('SELECT name FROM characters')

names = c.fetchall() # returns a list of tuples

print("Brave Adventurers:")
character_names = [] # sets up an empty list...

for name in names:
    print(name[0])
    character_names.append(name[0]) # adds that string to a list of student names

character_name = " "

while character_name not in character_names:
    print("Enter the name of an adventurer to see their weapons:")
    character_name = input(">>").title() # ensures the first letter of our user input is capitalized to test against our list.

c.execute('''
    SELECT weapons.name
    FROM weapons
    JOIN characters ON characters.id = weapons.characters_id
    JOIN characters ON characters.id = weapons.weapons_id
    WHERE characters.name = ?''', (character_name,))

weapons = c.fetchall()
print(f"{character_name} is wielding the following weapons:")
for weapon in weapons:
    print(weapon[0])

