#!/usr/bin/env python3

import requests
from datetime import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(URL).json()
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    epoch = resp["timestamp"]
    datetime_obj=datetime.fromtimestamp(epoch)
    coords_tuple = (lat,lon)
    result = rg.search(coords_tuple, verbose=False)
    city = result[0]['name']
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {datetime_obj}")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    print(f"City: {city}")
    
if __name__ == "__main__":
    main()
