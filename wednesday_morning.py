#!/usr/bin/env python3

''' This program to get full address from given IP address using API '''

import requests

#GLOBA
IPAPIURI = "http://ip-api.com/json/"

def main():
    # open file in read mode
    with open("ipaddress.txt", "r") as ipfile:
        # indent to keep the devicefile object open
        # loop across the lines in the file
        rcfile = open("addresses.txt", "w") 
        for ip in ipfile:
            #print and end without a newline
            finalURI = IPAPIURI + ip.rstrip()
            res = requests.get(finalURI)
            if res.status_code != 200:
                print("Status Error! Try Again!!")
            else:
                addrJson = res.json()
                print(f"IP Address: {ip}Address: {addrJson.get('as')}, {addrJson.get('city')}, {addrJson.get('regionName')}, {addrJson.get('country')}, {addrJson.get('zip')}\n")
                print("IP Address: " + ip + "Address: " + addrJson.get('as'), addrJson.get('city'), addrJson.get('regionName'), addrJson.get('country'), addrJson.get('zip'), file=rcfile)
                print("\n", file=rcfile) 
        rcfile.close()

if __name__ == "__main__":
    main()
