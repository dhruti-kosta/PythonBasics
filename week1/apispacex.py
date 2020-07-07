                                                                        #i#!/usr/bin/env python3

'''
This program harvests Spacex data available from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
'''

# using std library method for getting API data
import urllib.request
import json
from colorama import init,Fore, Back, Style

init()


# Global/ Constant of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():

    #Create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coredata = urllib.request.urlopen(SPACEXURI)
 
    xString = coredata.read().decode()
    print(type(xString))
    
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    displayString = ""
    for core in listOfCores:
        displayString += f"{Fore.GREEN}Core Serial: {Fore.WHITE}{core.get('core_serial')}\n{Fore.GREEN}Original Launch: {Fore.WHITE}{core.get('original_launch')}\n{Fore.GREEN}Details: {Fore.WHITE}{core.get('details')}\n{Fore.GREEN}Status: {Fore.WHITE}{core.get('status')}" 
        
        listOfMissions = core.get("missions")
        if (len(listOfMissions) > 0):
            displayString += f"\n{Fore.GREEN}Missions:"

            for mission in listOfMissions:
                displayString += f"\n\t{Fore.YELLOW}Name: {Fore.WHITE}{mission.get('name')}, {Fore.YELLOW}Flight: {Fore.WHITE}{mission.get('flight')}"

        displayString += "\n\n"

    print(displayString)
    

if __name__ == "__main__":
    main() 
