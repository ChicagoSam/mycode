#!/usr/bin/env python3

"""random joke generator as delivered by pirates"""

import requests
import pprint
from arrr import translate


# Source API
joke = "https://official-joke-api.appspot.com/random_joke"

tite = "\nWelcome to the Drunken Sailor, where every stand up comedian is a pirate!\n"
pirate = translate(title)
print(title)

# Random Jokes
def main():
    while True:
        #user y or n to continue
        perform = input("Would you like to hear a joke? y or n?\n")
        perform=perform.lower().strip() #normalize
        
        if perform == "y":
            resp = requests.get(joke)
            delivery = resp.json()
            print(delivery['setup'])
            print(delivery['punchline'])
            #english = print(delivery['setup'])
            #arrr.main(arrrgv=english)
            #english = print(delivery['punchline'])
            #arrr.translate(english)
            continue

        elif perform == "n":
            print()
            print("Thank you for coming out tonight! Remember to tip your server!")
            break


        else:
            print("Please type 'y' or 'n'") #only allow y/n

if __name__ == "__main__":
    main()
