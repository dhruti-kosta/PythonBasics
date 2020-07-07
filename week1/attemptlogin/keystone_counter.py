#!/usr/bin/python3

import re

def main():
    #parse keystone.common.wsgi and return number of failed & successful login attempts
    loginfail = 0 # counter for fails
    loginsuccess = 0 # counter for success
    listOfFailedIPs = []
    
    # open the file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
    
    # turn the file into a list of lines in memory
    keystone_file_lines=keystone_file.readlines()
    
    # loop over the list of lines
    for line in keystone_file_lines:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            listOfFailedIPs.append(line.split(" ")[-1]) 
            
       # if "-] Authorization failed" in line:
           # loginsuccess += 1 # this is the same as loginsuccess = loginsuccess + 1
        
        if re.search("-] Authorization failed", line):
            loginsuccess += 1


    print("The number of failed log in attempts is", loginfail)
    for ip in listOfFailedIPs:
        print(ip.rstrip("\n"))
    
    print("The number of successful log in attempts is", loginsuccess - loginfail)

    keystone_file.close() # close the open file

if __name__ == "__main__":
    main()
