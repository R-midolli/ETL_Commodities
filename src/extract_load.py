#import libraries
import yfinance as yf
import pandas as pd
from dotenv import load_dotenv
import os

#import ambient variables

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

if __name__ == "__main__":
    concatenated_data = search_all_data(commodities)
    print(concatenated_data)

