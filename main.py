
import requests
from bs4 import BeautifulSoup
import pandas as pd

def pokemon_names_df():
    """
    This function will scrape the names of Generation 2 Pokemon from the Wikipedia page and save them to a CSV
    file.
    """
    # wiki url
    url = "https://en.wikipedia.org/wiki/List_of_generation_II_Pok%C3%A9mon"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # find pokemon names in HTML
    pokemon_names_html = soup.find("div", class_ = "toc plainlinks toc-top")

    # empty list to store all pokemon names
    pokemon_names = []
    
    # extract names in pokemon_names_html and append to empty pokemon names list
    for names in pokemon_names_html:
        pokemon_names.append(names.get_text())
            
    pokemon_names = pokemon_names[3][1:-1].split("\n")

    # create dictionary for pokemon names
    pokemon_data = {
                    "Pokemon Names": pokemon_names
                    }

    # convert to pandas dataframe
    pokemon_names_data_df = pd.DataFrame(pokemon_data)

    # convert to csv file
    pokemon_names_data_df.to_csv("pokemon_gen_2_names.csv", index = False)
    
    return pokemon_names_data_df

pokemon_names_df()
