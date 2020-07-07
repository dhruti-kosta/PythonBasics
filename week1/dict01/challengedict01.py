#!/usr/bin/env python3


# rather than copy and paste our data into our script
# we placed it in a file
# that file (spacex.data) is LEGAL json
# python is DUMB, and thinks it is plain text
# we can overcome this issue with the json lib
import json
import requests
# Challenge Exercise - Dictionaries

def main():
    # open the JSON file spacex.data with the handle jsonfile
    #with open("spacex.data", "r") as jsonfile:
     #   spacexdata = json.load(jsonfile)  # use the json library to LOAD our json data into python
                                          # this causes python to recognize the lists and dicts
                                          # rather than "just" see plain text

    r = requests.get("https://api.spacexdata.com/v3/capsules") 
    spacexdata = r.json()

    #print(spacexdata)  # print out the list of spacex data
    #print(spacexdata.count('capsule_serial'))

    # display all data
    print("Display all data")
    for item in spacexdata:
        print(item)

    # display all capsule serials
    print("Display all capsule serials")
    for item in spacexdata:
        print(item.get("capsule_serial"))

    # display all capsule serials & original launch
    print("Display all capsule serials & original launch")
    for item in spacexdata:
        if not item.get("original_launch"):
            print(item.get("capsule_serial"), "has not yet launched!")
        else:
            print(item.get("capsule_serial")+ " - " + item.get("original_launch")) 

    #display total no of launches
    print("Display total number of launches & landings")
    count = 0
    totallandings = 0
    for item in spacexdata:
        if item.get("original_launch"):
            count += 1
        if item.get("landings"):
            totallandings += item.get("landings")
        
    print("total no of launches: ", count)
    print("total no of landings: ", totallandings)

    #display capsule types
    print("Display all capsule types")
    typeslist = []
    for item in spacexdata:
        if not typeslist.count(item.get("type")):
            typeslist.append(item.get("type"))
    print(typeslist)

if __name__ == "__main__":
    main()
