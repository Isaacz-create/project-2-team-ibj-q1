This project scrapes a table with Pokemon names from the Pokemon Wikipedia and stores the results in a dataframe.
The primary goal is to retrieve data about Pokemon such as their names, pokedex number, ability, hp, type, attack, and defense.

The script works by calling a function that uses the scraped names from Wiki as parameters. It uses the names make requests towards the Pokemon API to grab information.
It uses Python to convert the data from the webpage and API to dictionaries, then to CSV files. It combines the scraped data and API data to merge into a single dataframe for analysis. This project requires libraries such BeautifulSoup, json, requests, sqlite3 and pandas.

This project helps address common issues such as selecting certain Pokemon for battle strategies. Through multiple sources of data, there is comparison across key attributes.
This analysis can assist and help players to help them gain advantage by understanding certain trends in Pokemon design.


Author: Brian Chum
Fixed Errors/Bugs, Cleaned up script/data: Isaac Zhong, Jahmar Lawrence
