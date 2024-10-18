#importing the necessary libraries
import yfinance as yf
import pandas as pd

# List of principal metal commodities symbols
metal_symbols = [
    "GC=F",  # Gold
    "SI=F",  # Silver
    "HG=F",  # Copper
    "PL=F",  # Platinum
    "PA=F",  # Palladium
    "ALI=F", # Aluminum
]

# Create an empty DataFrame to store the data
metals_df = pd.DataFrame()

# Fetch data for each metal commodity
for symbol in metal_symbols:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="5y")  # Fetch 5 years of data
    
    # Extract the closing price and add it to the DataFrame
    metals_df[symbol] = data['Close']

# Reset the index to make the date a column
metals_df.reset_index(inplace=True)

# Rename columns for clarity
metals_df.rename(columns={
    "GC=F": "Gold",
    "SI=F": "Silver",
    "HG=F": "Copper",
    "PL=F": "Platinum",
    "PA=F": "Palladium",
    "ALI=F": "Aluminum",
    "Date": "Date"
}, inplace=True)

# Ensure only the specified columns are in the DataFrame
metals_df = metals_df[["Date", "Gold", "Silver", "Copper", "Platinum", "Palladium", "Aluminum"]]

# Display the first few rows of the DataFrame
print(metals_df.head())

# Optionally, save the DataFrame to a CSV file

# metals_df.to_csv("metal_commodities_data.csv", index=False)
