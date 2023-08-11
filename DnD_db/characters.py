#!/usr/bin/python3
"""Sammy Tamimi | SQLite miniproject using D&D party"""

import sqlite3

# Create a connection to a new SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create the characters table with columns for Character ID and Character Name
c.execute('''CREATE TABLE IF NOT EXISTS characters
             (id INTEGER PRIMARY KEY,
              name TEXT)''')

# Characters
c.execute("INSERT INTO characters (id, name) VALUES (1, 'Longspear Lux')")
c.execute("INSERT INTO characters (id, name) VALUES (2, 'Bruno Breakbone')")
c.execute("INSERT INTO characters (id, name) VALUES (3, 'Cyrus Sevenfingers')")
c.execute("INSERT INTO characters (id, name) VALUES (4, 'Rho of the Red Ice')")
c.execute("INSERT INTO characters (id, name) VALUES (5, 'Thunk')")
c.execute("INSERT INTO characters (id, name) VALUES (6, 'Atavisk')")

# Commit changes and close the connection
conn.commit()
conn.close()
