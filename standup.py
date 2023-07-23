#!/usr/bin/env python3

"""random joke generator as delivered by pirates"""
import os
import requests
import pprint
from arrr import translate


# Source API
joke = "https://official-joke-api.appspot.com/random_joke"

# Intro
os.system('clear') # Clearing Screen
f= open ('pirateship.txt','r')
print(''.join([line for line in f]))  #print ship
title = "Welcome to the Drunken Sailor, where every comedian is a pirate!\n"
pirate = translate(title) # translates to pirate
print(title)

# Random Jokes in Pirate
def main():
    while True:
        # user yay or nay to continue
        question = "Would you like to hear a joke, my friend?"
        pirate = translate(question) # translates to pirate
        print() # formatting for looping back after joke
        print(pirate)
        perform = input("yay or nay?\n>")
        perform=perform.lower().strip() # normalize
        
        if perform == "yay":
            resp = requests.get(joke)
            delivery = resp.json()
            
            # Setup
            print()
            setup = (delivery['setup'])
            pirate = translate(setup) # translates to pirate
            print(pirate)

            # Punchline
            print()
            punchline = (delivery['punchline'])
            pirate = translate(punchline) # translates to pirate
            print(pirate)

        elif perform == "nay":
            print()
            outro = "Thank you for coming out tonight! Remember to tip your server!"
            pirate = translate(outro) # translates to pirate
            print(pirate)
            break

        else:
            print("Ye scallywag! Please type 'yay' or 'nay'!") # only allow yay/nay

if __name__ == "__main__":
    main()
