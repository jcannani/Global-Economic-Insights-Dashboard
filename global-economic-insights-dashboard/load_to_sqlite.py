import pandas as pd
import sqlite3

# Load the cleaned dataset
df = pd.read_csv('cleaned_bank_data.csv')

# Connect to SQLite database (it will create one if it does not exist)
conn = sqlite3.connect('world_bank.db')

# Write data to a table
df.to_sql('World_bank', conn, if_exists="replace", index=False)

print('Data loaded into SQLite database successfully.')

# Check the first few rows
df = pd.read_sql_query("SELECT * FROM world_bank LIMIT 5;", conn)
print(df.head())

# Different SQL Queries 
df = pd.read_sql_query("SELECT country_name, 'GDP (Current USD)"
                       FROM world_bank)