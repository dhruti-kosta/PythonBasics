#~/usr/bin/env python3
import requests
import pandas
import json
from colorama import Fore,Style,init
init()

# GLOBAL
API = "https://statsapi.web.nhl.com/api/v1/teams"

def main():
    # call the webservice
    res = requests.get(API)
    # print the response json
    print(res.json())

    # display names of teams
    print(f"\n{Fore.GREEN}{Style.BRIGHT}Team Names::")
    teams = res.json().get("teams")
    count = 1
    for team in teams:
        print(f"{Fore.GREEN}{Style.BRIGHT}Team {count}. ")
        print(f"\t{Style.BRIGHT}{Fore.WHITE}Name: {Style.NORMAL}{team.get('name')}")
        print(f"\t{Style.BRIGHT}Abbreviation: {Style.NORMAL}{team.get('abbreviation')}")
        print(f"\t{Style.BRIGHT}Team Name: {Style.NORMAL}{team.get('teamName')}")
        print(f"\t{Style.BRIGHT}Location Name: {Style.NORMAL}{team.get('locationName')}")
        print(f"\t{Style.BRIGHT}First Year of Play: {Style.NORMAL}{team.get('firstYearOfPlay')}")
        print(f"\t{Style.BRIGHT}Official Site URL: {Style.NORMAL}{team.get('officialSiteUrl')}")
        print(f"\t{Style.BRIGHT}Active: {Style.NORMAL}{team.get('active')}")
        count += 1

    itemsdf = pandas.DataFrame(teams)
    itemsdf.to_excel("teams.xlsx")
    itemsdf.to_csv("teams.csv")
    itemsdf.to_json("teams.json", orient='records')

if __name__ == "__main__":
    main()
