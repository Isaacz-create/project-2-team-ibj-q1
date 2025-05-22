import requests
import pandas as pd
from main import pokemon_names_df
from pokemon_data import pokemon_info_df
import sqlite3

# Call the functions to get the DataFrames
names_df = pokemon_names_df()
info_df = pokemon_info_df(names_df["Pokemon Names"].tolist())

# Merge dataframes using pd.concat
merged_df = pd.concat([names_df, info_df], axis=1)

# Display merged dataframe
print(merged_df.head())

# Display descriptive stats
print(merged_df.describe())

# Export to CSV
merged_df.to_csv('pokemon.csv', index=False)

# Export to SQLite database
db_conn = sqlite3.connect("pokemon.db")
merged_df.to_sql("Pokemon_Data", db_conn, if_exists="replace", index=False)
