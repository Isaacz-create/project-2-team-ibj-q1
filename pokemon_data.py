
import requests
import pandas as pd
from main import pokemon_names_df

def pokemon_info_df(pokemon_names):
    """
    This function will fetch detailed info for each generation 2 Pokemon name passed in the pokemon_names
    list using the PokéAPI and save that data as a CSV.
    """
    
    # empty lists to store data
    pokedex_id_list = []
    pokemon_type_list = []
    ability_list = []
    hp_list = []
    attack_list = []
    defense_list = []

    
    for pokemon in pokemon_names:
        # make new api call for each pokemon
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        r = requests.get(url)
        
        # only parse the json for pokemon that had successful api call
        if r.status_code == 200:
            data = r.json()

            # look into json for specific parameters and store each in a variable
            pokedex_id = data["id"]
            pokemon_type = data["types"][0]["type"]["name"]
            ability = data["abilities"][0]["ability"]["name"]
            hp = data["stats"][0]["base_stat"]
            attack = data["stats"][1]["base_stat"]
            defense = data["stats"][2]["base_stat"]

            # put into the empty lists
            pokedex_id_list.append(pokedex_id)
            pokemon_type_list.append(pokemon_type)
            ability_list.append(ability)
            hp_list.append(hp)
            attack_list.append(attack)
            defense_list.append(defense)

        else:
            # Makes sure each pokemon name is found
            print(f" Error {pokemon} not found")

    # create dictionary with data
    pokemon_data = {
                    "Pokedex Number": pokedex_id_list,
                    "Type": pokemon_type_list,
                    "Ability": ability_list,
                    "HP": hp_list,
                    "Attack": attack_list,
                    "Defense": defense_list
                }

    # convert to pandas dataframe
    pokemon_info_df = pd.DataFrame(pokemon_data)

    # export to CSV
    pokemon_info_df.to_csv("pokemon_gen_2_data.csv", index=False)

    return pokemon_info_df

# get the names from create_pokemon_generation_2_names_df()
pokemon_names = pokemon_names_df()["Pokemon Names"].tolist()

# print parameters and create CSV file
pokemon_info_df(pokemon_names)
