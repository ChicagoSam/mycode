#!/usr/bin/python3

import requests

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    # create a list to store items with the word "heal"
    icewords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the word heal
        if 'ice' in item.get("name"):
            # if TRUE, add that item to the end of list healwords
            icewords.append(item.get("name"))

    ## list all
    print(f"There are {len(icewords)} words that contain the word 'ice' in the Pokemon Item API!")
    print("List of Pokemon items containing ice: ")
    print(icewords)

if __name__ == "__main__":
    main()

