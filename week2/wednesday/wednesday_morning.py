#~/usr/bin/env python3
import requests
import webbrowser
import pandas

# GLOBAL
NORADAPI = "http://www.celestrak.com/NORAD/elements/active.txt"

def main():
    # call the webservice with our key
    res = requests.get(NORADAPI)
    if res.status_code != 200:
        print("Status Error! Try Again!!")
    else:
        # save response in .txt file
        with open('data.txt', 'w') as f:
            f.writelines(res.text)
       
        satellitelist = []
        fl = open('data.txt', 'r')
        for index, line in enumerate(fl.readlines()):
            if (index%3 == 0) & (line != '\n'):
                satellitelist.append(line.strip("\n"))

        # data = pandas.read_fwf('data.txt', sep="\n", header=None)
        # for row in data.to_dict(orient='records'):
        #     if (row[0]):
        #         satellitelist.append(d.strip("\n"))

        # write names in file
        with open('names.txt','w') as names:
            names.writelines("%s\n" % l for l in satellitelist)

        # print names using list
        #print(satellitelist)

if __name__ == "__main__":
    main()
