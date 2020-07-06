#!/usr/bin/python3

import requests
import pandas
# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()
    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")
    print(pokemon)
    
    # Loop through data, and print pokemon names
    pokemon_plain = ''
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        pokemon_plain += poke.get("name") + ","
    print(pokemon_plain)
    
    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(pokemon["results"])
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_html("pokemons.html")

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(pokemon["results"])
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_json("pokemons.json")

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(pokemon["results"])
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemons.xlsx", index=False)

if __name__ == "__main__":
    main()
