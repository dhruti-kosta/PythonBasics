#!/usr/bin/env python3

# python3 -m pip install pyyaml
import yaml

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
    with open("work2do.yml", "r") as df:
       # load yaml data into work2do
        work2do = yaml.load(df, Loader=yaml.FullLoader)

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

