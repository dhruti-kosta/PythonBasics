#~/usr/bin/env python3
import requests

def main():
    for i in range(0,51):
        res = requests.get("http://0.0.0.0:2224/fast")
        if res.status_code != 200:
            print("429:Maximum requests reached!! 200 Per Day, 50 Per Hour Allowed.")
        else:
            print("I inherit the default limits of 200 per day and 50 per hour.")

if __name__ == "__main__":
    main()
