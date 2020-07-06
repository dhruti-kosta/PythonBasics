#!/usr/bin/python3

import requests

# define the URL we want to use
CODEURL = "http://code.jsontest.com"
MD5URL = "http://md5.jsontest.com/?text=MonsterGame"

def main():
    ## PART A
    ## pull a code object from code.jsontest.com
    # make the request
    resp = requests.get(CODEURL)
    # pull json off 200 response
    print(resp.text)

    ## PART B
    ## pull a md5 object from md5.jsontest.com
    # make the request
    resp = requests.get(MD5URL)
    # pull json off 200 response
    print(resp.text)

if __name__ == "__main__":
    main()
