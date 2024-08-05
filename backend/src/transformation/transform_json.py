import pandas as pd
from io import StringIO
from datetime import datetime

def transform_json(input_file, output_file):

        # Leia o arquivo JSONL para um DataFrame pandas
    with open(input_file, 'r') as file:
        data = file.read()

    df = pd.read_json(StringIO(data), lines=True)

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

    # Save the transformed data to a new JSONL file
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)
    print(f"Transformed data saved to {output_file}")

if __name__ == "__main__":
    transform_json("../data/data.jsonl", '../data/transformed_data.json')
