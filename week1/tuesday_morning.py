'''
This program get json data from API http://api.open-notify.org/iss-now.json using Python standard library methods

Display Date, location address from Lat, Long  
'''

import requests
from datetime import datetime
from geopy.geocoders import Nominatim

def main():
    # Grab ISS data
    res = requests.get("http://api.open-notify.org/iss-now.json")
    if res.status_code != 200:
        print("Status Error, Please try again!")
    else:
        issdata = res.json()

        # Date conversion
        date = datetime.fromtimestamp(issdata.get("timestamp"))
        print("Date: " , date)

        # Get ISS position (lat / lon)
        issposition = issdata.get("iss_position")
        print("ISS Position:" , issposition)
        longitude = issposition.get("longitude")
        latitude = issposition.get("latitude")

        # Get location from lat, long using geopy library
        geolocator = Nominatim(user_agent="myGeocoder")
        try:
            location = geolocator.reverse(f"{latitude}00, {longitude}00")
            print("Location: ", location.address)
        except Exception:
            print("Location error")


if __name__ == "__main__":
    main()
