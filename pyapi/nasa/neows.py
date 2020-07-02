#~/usr/bin/env python3
import requests

# GLOBAL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    # define credentials
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")
    startdate = "start_date=" + input("Enter Start Date: ") 
    enddate = "end_date=" + input("Enter End Date: ")

    # call the webservice with our key
    URI = NEOURL + startdate + "&"  + enddate + "&" + nasacreds
    res = requests.get(URI)
    if res.status_code != 200:
        print("Status Error! Try Again!!")
    else:
        neodata = res.json()
        for link in neodata["links"]:
            print(link)
        print()
        print(neodata["near_earth_objects"])
        
if __name__ == "__main__":
    main()
