"""Sammy Tamimi | SQLite miniporject using D&D party"""

import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Query all products that XYZ Corp provides
c.execute('''
          SELECT name
          FROM weapons
          WHERE characters_id = (
              SELECT id
              FROM characters
              WHERE name = 'Bruno Breakbone'
          )
          ''')

# Fetch the results and print them
results = c.fetchall()
for row in results:
    print(row[0])

# Close the connection
conn.close()
