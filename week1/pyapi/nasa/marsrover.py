#~/usr/bin/env python3
import requests
import webbrowser
from dotenv import load_dotenv
load_dotenv()
import os

# GLOBAL
NASAAPI = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=NAVCAM&"

def main():
    # define credentials
    # option 1
    API_KEY = os.getenv("API_KEY")
    nasacreds = "api_key=" + API_KEY
    # option 2
    #with open("/home/student/nasa.creds") as mycreds:
        #nasacreds = mycreds.read()
    #nasacreds = "api_key=" + nasacreds.strip("\n")

# call the webservice with our key
    res = requests.get(NASAAPI + nasacreds)
    if res.status_code != 200:
        print("Status Error! Try Again!!")
    else:
        marsroverdata = res.json()
        for photo in marsroverdata["photos"]:
            print(photo)
            print()
            #webbrowser.open_new_tab(photo["img_src"])

if __name__ == "__main__":
    main()
