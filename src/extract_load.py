#import libraries
import yfinance as yf
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

#import ambient variables
load_dotenv()

#import database variables
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASSWORD = os.getenv('DB_PASSWORD_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')
DB_THREADS = os.getenv('DB_THREADS_PROD')
DB_TYPE = os.getenv('DB_TYPE_PROD')

DB_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)

# list of commodities to extract
commodities = ["CL=F","GC=F", "SI=F", "HG=F", "PL=F", "PA=F", "ALI=F"]

#create a function to extract data from yahoo finance
def search_commodities_data(toten, period = '5y', interval='1d'):
    ticker = yf.Ticker(toten)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['toten'] = toten
    return data

#concatenate all the commodities data
def search_all_data(commodities):
    all_data = []
    for toten in commodities:
        data = search_commodities_data(toten)
        all_data.append(data)
    return pd.concat(all_data)

#load the data to postgres
def load_data_to_postgres(df, schema=DB_SCHEMA):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

if __name__ == "__main__":
    concatenated_data = search_all_data(commodities)
    load_data_to_postgres(concatenated_data, schema=DB_SCHEMA)
    print("Data loaded to postgres")
