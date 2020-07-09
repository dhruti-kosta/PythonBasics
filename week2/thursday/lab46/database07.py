#!/usr/bin/env python3

'''
This program harvests Spacex data available from https://api.spacexdata.com/v3/cores using the Python Standard Library methods

Insert those data into database using sqlite3
Extract data from database
'''

# using std library method for getting API data
import requests
import sqlite3
from datetime import datetime
import dateutil.parser

# Global/ Constant of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():

    #Create a requests response object by sending an HTTP GET to SPACEXURI
    coredata = requests.get(SPACEXURI).json()
    
    # Create database and table called SPACEXDATA
    conn = sqlite3.connect('spacex.db')
    print("Opened database 'spacex.db' successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS SPACEXDATA
     (SPACEXID INTEGER PRIMARY KEY AUTOINCREMENT,
     CORE_SERIAL           TEXT    NOT NULL,
     STATUS            TEXT     NOT NULL,
     LAUNCHDATE        TEXT,
     MISSIONSCOUNT      INT,
     DETAILS         TEXT);''')
    print("Table 'SPACEXDATA' created successfully")
    
    # Insert data from API into newly created table SPACEXDATA
    for core in coredata:
        conn.execute("INSERT OR REPLACE INTO SPACEXDATA (SPACEXID, CORE_SERIAL, STATUS, LAUNCHDATE, MISSIONSCOUNT, DETAILS) VALUES ((select SPACEXID from SPACEXDATA where CORE_SERIAL = '" + core.get('core_serial') + "'),?,?,?,?,?)", (core.get('core_serial'), core.get('status'), dateutil.parser.parse(core.get('original_launch')).strftime('%m/%d/%Y'), len(core.get('missions')), str(core.get('details'))))
        conn.commit()
    print("Records inseted successfully")
    
    # Print data from table SPACEXDATA
    cursor = conn.execute("SELECT SPACEXID, CORE_SERIAL, STATUS, LAUNCHDATE, MISSIONSCOUNT, DETAILS from SPACEXDATA")
    for row in cursor:
        print("SPACEX ID = ", row[0])
        print("CORE SERIAL = ", row[1])
        print("STATUS = ", row[2])
        print("LAUNCH DATE = ", row[3])
        print("MISSIONS COUNT = ", row[4])
        print("DETAILS = ", row[5], "\n")
    print("Operation done successfully")
    
    cursor = conn.execute("SELECT COUNT(*) from SPACEXDATA")
    for row in cursor:
        MAX_ID = row[0]
    id = input(f"Choose ID [1 - {MAX_ID}] to check data -> \n")
    cursor = conn.execute("SELECT SPACEXID, CORE_SERIAL, STATUS, LAUNCHDATE, MISSIONSCOUNT, DETAILS from SPACEXDATA WHERE SPACEXID=" + id)
    for row in cursor:
        print("SPACEX ID = ", row[0])
        print("CORE SERIAL = ", row[1])
        print("STATUS = ", row[2])
        print("LAUNCH DATE = ", row[3])
        print("MISSIONS COUNT = ", row[4])
        print("DETAILS = ", row[5], "\n")

    conn.close()

if __name__ == "__main__":
    main()
