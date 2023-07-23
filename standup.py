#!/usr/bin/env python3

"""random joke generator as delivered by pirates"""

import requests
import pprint
from arrr import translate


# Source API
joke = "https://official-joke-api.appspot.com/random_joke"

title = "\nWelcome to the Drunken Sailor, where every stand up comedian is a pirate!\n"
pirate = translate(title)
print(title)

# Random Jokes in Pirate
def main():
    while True:
        #user y or n to continue
        question = "Would you like to hear a joke, my friend?"
        pirate = translate(question)
        print(pirate)
        perform = input("yay or nay?\n>")
        perform=perform.lower().strip() #normalize
        
        if perform == "yay":
            resp = requests.get(joke)
            delivery = resp.json()
            
            setup = (delivery['setup'])
            pirate = translate(setup)
            print(pirate)

            punchline = (delivery['punchline'])
            pirate = translate(punchline)
            print(pirate)

        elif perform == "nay":
            print()
            print("Thank you for coming out tonight! Remember to tip your server!")
            break

        else:
            print("Ye scallywag! Please type 'yay' or 'nay'!") #only allow yay/nay

if __name__ == "__main__":
    main()
