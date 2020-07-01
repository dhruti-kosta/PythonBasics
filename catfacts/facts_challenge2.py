#!/usr/bin/env python3
"""Author: DKosta"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    if r.status_code != 200:
        print("Invalid status code! Try again!!")
    else:
        ## the code random select one cat fact 
        ## print the value associated with text"
        randomcatfact = random.choice(r.json()["all"])
        print(randomcatfact.get("text"))  # the .get() method returns NONE if key not found
main()
