
import requests
import pandas as pd
from main import pokemon_names_df
from pokemon_data import pokemon_info_df
import sqlite3

# DF1 and DF2 files to merge

names_df = pokemon_names_df()
pokemon_info = pokemon_info_df(names_df["Pokemon Names"].tolist())


#Merge dataframes using pd.concat

merged_df = pd.concat([pokemon_names_df, pokemon_info], axis = 1)


# display merged dataframe
print(merged_df.head())

# display descriptive stats
print(merged_df.describe())

#Export to CSV File

merged_df.to_csv('pokemon.csv', index=False)

#Convert DataFrame to SQL
db_conn = sqlite3.connect("pokemon.db")
merged_df.to_sql("Pokemon_Data", db_conn, if_exists="replace", index=False)
