#!/usr/bin/python3
import requests
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

url = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define creds
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## Call the webservice with our key
    resp = requests.get(f"{url}{nasacreds}").json()

    print(resp)


    print()

    print(resp["title"] + "\n")

    print(resp["date"] + "\n")

    print(resp["explanation"] + "\n")

    print(resp["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()

