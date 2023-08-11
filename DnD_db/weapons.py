#!/usr/bin/python3
"""Sammy Tamimi | SQL miniproject using DnD characters"""
 
import sqlite3
 
# Create a connection to a new SQLite database
conn = sqlite3.connect('my_database.db')
 
# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create the weapons table with columns for ID, Name, and Character ID
c.execute('''CREATE TABLE IF NOT EXISTS weapons
            (id INTEGER PRIMARY KEY,
             name TEXT,
             characters_id INTEGER,
             FOREIGN KEY(characters_id) REFERENCES characters(id))''')
 
# Weapons
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (1, 'Longspear', 1)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (2, 'Fists', 2)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (3, 'Longbow', 3)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (4, 'Double-Bladed Sword', 4)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (5, 'Heavy Mace', 5)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (6, 'Spiked Shield', 6)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (7, 'Dagger', 1)") 
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (8, 'Feet', 2)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (9, 'Short Sword', 3)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (10, 'Chakram', 4)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (11, 'Shortbow', 5)")
c.execute("INSERT INTO weapons (id, name, characters_id) VALUES (12, 'Sling', 6)")

# Commit changes and close the connection
conn.commit()
conn.close()

