#!/user/bin/env python3

"""Sammy Tamimi
Homework for 7/20: random numbers, opposed dice rolls, for loops, reading/writing to files"""


#Importing tools to use
import random

#Print random # from 1-6
print(f"This is a single random number: {random.randint(1,6)}\n")

#Print 2 random #s from 1-6
print(f"These are two random numbers: {random.sample(range(1,6), 2)}\n")


#Opposed d20 rolls, declare winner (or tie)
def rolloff():
    
    print("Nerd and Dork are rolling d20s against each other!")

    #Roll 2 d20 dice
    roll1 = random.randint(1,20)
    roll2 = random.randint(1,20)

    #If A wins
    if roll1 > roll2:
        print(f"And... Nerd rolled a {roll1}, beating Dork's {roll2}!")
    
    #If B wins
    elif roll2 > roll1:
        print(f"And... Dork rolled a {roll2}, beating Nerd's {roll1}!")

    #If tie roll
    elif roll1 == roll2:
        print(f"And... Nerd and Dork tied with the same roll of {roll1}!")
        #print("They must roll again!")
    
        #rolloff()

    print("What an exciting roll off!\n")

rolloff()

#Looping Exercise


# can you loop over this list and print "<hero name> is great!"
heroes= ["Batman","Spiderman","Catwoman","Alfred Pennyworth"]

print("This is a list of great freakin' characters:")

for char in heroes:
    print(f"{char} is great!")
    
print()

# can you loop over this list of dictionaries are print: "<hero name>'s power is <power>"
hero_dict= [{"name": "Batman", "powers": "being the world's greatest detective"},
            {"name": "Spiderman", "powers": "web shooting"},
            {"name": "Catwoman", "powers": "burglary"},
            {"name": "Alfred Pennyworth", "powers": "being super butler"}
           ]

print("This is a list of heroes and their powers:")

#List of Heroes and their power
for hero in hero_dict:
    name = hero["name"]
    powers = hero["powers"]
    print(f"{name}'s power is {powers}.")

#READ/WRITE TO FILES

#wget https://raw.githubusercontent.com/csfeeser/Python/master/TLG/devops/simpledoc.txt

print="use the open() function to access the file simpledoc.txt"
print="read out the contents of the file and print it to the screen"

#def readbook():
    #book = open('simpledoc.txt', 'r')
    #print(book.read()) 
    #book.close()

#readbook()

#print="convert the file to a list, print the list"

#def listprintbook():
    #book2 = open('simpledoc.txt', 'r')
    #print(book2.read())
    #book2.seek(0)
    #book2_list = book.readlines()
    #for x in book2_list:
        #print(x)
    #book2.close

#listprintbook()

#add a new line to the bottom of the poem (use the "a" permission!)
