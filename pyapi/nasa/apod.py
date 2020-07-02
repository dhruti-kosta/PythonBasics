#~/usr/bin/env python3
import requests
import webbrowser

# GLOBAL
NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    # define credentials
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")

    # call the webservice with our key
    res = requests.get(NASAAPI + nasacreds)
    if res.status_code != 200:
        print("Status Error! Try Again!!")
    else:
        apod = res.json()
        print(apod["title"] + "\n")
        print(apod["date"] + "\n")
        print(apod["explanation"] + "\n")
        print(apod["url"])
        webbrowser.open(apod["url"])

if __name__ == "__main__":
    main()
