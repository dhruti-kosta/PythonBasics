#!/usr/bin/env python3

def main():
    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")
    # close your file
    dnsfile.close()
     
if __name__ == "__main__":
    main()
