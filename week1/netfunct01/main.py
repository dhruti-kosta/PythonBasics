#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here


# function to reboot device
def devicereboot(ips): # ips==list
    for ip in ips:
        print('\nConnecting to... ' + ip)
        print('REBOOTING NOW!')
        


# start our main script
def main():

    # open file in read mode
    with open("work2do.txt", "r") as devicefile:
        # indent to keep the devicefile object open
        # loop across the lines in the file
        
        for dev in devicefile:
            #print and end without a newline
            print(dev, end="")
    # no need to close our file - closed automatically


    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1": ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

    ## call device reboot function
    devicereboot(work2do.keys())

# call our main function
if __name__ == "__main__":
    main()

