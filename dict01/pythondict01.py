#!/usr/bin/env python3

# Lab 11 - Dictionaries

def main():
    ## create a dictionary
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display parts of the dictionary
    print(switch["hostname"])
    print(switch["ip"])

    ## request a 'fake' key
    ## print(switch["fake"])  

    ## request a 'fake' key with .get() method
    print("First Test - .get()")
    print(switch.get("fake"))

    print("Second Test = .get()")
    print(switch.get("fake", "The Key is in another castle!"))

    print("Third Test -.get()")
    print(switch.get("version"))

    print("Fourth Test - .keys()")
    print(switch.keys())

    print("Fifth Test - .values()")
    print(switch.values())

    print("Sixth Test - .pop()")
    switch.pop("version") # removes this key (and value) pair
    print(switch.keys())   # notice the value of version is gone
    print(switch.values()) # notice the value 1.2

    print("Seventh Test - ADD a new value")
    switch["adminlogin"] = "karl08"
    print(switch.keys())
    print(switch.values())

    print("Eighth Test - ADD a new value")
    switch["password"] = "qwerty"
    print(switch.keys())
    print(switch.values())


if __name__ == "__main__":
    main()
