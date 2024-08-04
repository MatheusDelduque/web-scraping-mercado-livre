import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from datetime import datetime

# Load environment variables
load_dotenv()

# Define the path to the JSONL file
json_file_path = "../../data/data.jsonl"

# Read the JSONL file into a pandas DataFrame
df = pd.read_json(json_file_path, lines=True)

# Add a new column with the source URL
df["_source"] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

# Add a new column with the collection date
df["_collection_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Clean up the data
df["brand"] = df["brand"].fillna("")
df["reviews_rating_number"] = df["reviews_rating_number"].fillna("0").astype(float)
df["old_price"] = df["old_price_reais"].astype(float) + df["old_price_cents"].astype(float).fillna(0) / 100
df["new_price"] = df["new_price_reais"].astype(float) + df["new_price_cents"].astype(float).fillna(0) / 100
df['reviews_amount'] = df['reviews_amount'].str.replace('(', '').str.replace(')', '')
df['reviews_amount'] = df['reviews_amount'].fillna('0').astype(int)

# Drop unnecessary columns
df = df.drop(columns=['old_price_reais', 'old_price_cents', 'new_price_reais', 'new_price_cents'])

# Print the resulting DataFrame
print(df)

# Save the DataFrame to a PostgreSQL database
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
table_name = os.getenv('TABLE_NAME')

connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_string)

df.to_sql(table_name, engine, if_exists='replace', index=False) 