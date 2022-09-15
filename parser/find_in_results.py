import sqlite3
import pandas as pd

cnx = sqlite3.connect('result_db.db')

df = pd.read_sql_query("SELECT * FROM result", cnx)

pokemon_games = df.loc[df['NAME'].str.contains("OMETH", case=False)]

print(pokemon_games.to_string())