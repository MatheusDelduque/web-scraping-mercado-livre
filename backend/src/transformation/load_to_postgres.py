import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

def load_to_postgres(json_file):
    
    # Read the JSON file into a pandas DataFrame
    df = pd.read_json(json_file, orient='records', lines=True)

    # Define the database connection parameters
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    table_name = os.getenv('TABLE_NAME')

    # Define the connection string
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Create the database engine
    engine = create_engine(connection_string)

    # Save the DataFrame to the database
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data inserted into the {table_name} table of the {db_name} database.")

if __name__ == "__main__":
    load_to_postgres('../data/transformed_data.json')
