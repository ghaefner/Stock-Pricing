from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame, read_csv, merge
from io import StringIO
from conf import AV_API_KEY, BASE_URL, STOCK


# Functins to access stock data
def get_timeseries(stock_label: str, periodicity = "daily", currency = "USD") -> DataFrame:
    
    if periodicity not in ["daily", "weekly", "monthly"]:
        print("No correct periodicity provided. Daily stock prices are used as default.")
        periodicity = "daily"
    
    # Get stock time series data
    full_url_stock = f"{BASE_URL}function=TIME_SERIES_{periodicity.upper()}&symbol={stock_label}&apikey={AV_API_KEY}&datatype=csv"
    r = requests.get(full_url_stock).content
    stock_data = read_csv(StringIO(r.decode("utf-8")))

    # Get foreign exchange data
    if (currency != "USD"):
        full_url_fex_rate = f"{BASE_URL}function=FX_{periodicity.upper()}&from_symbol=USD&to_symbol=EUR&apikey={AV_API_KEY}&datatype=csv"
        r = requests.get(full_url_fex_rate).content
        fex_data = read_csv(StringIO(r.decode("utf-8")))

        # Merge the two dataframes on the 'timestamp' column
        merged_data = merge(stock_data, fex_data, on="timestamp", suffixes=("_stock", "_fex"))
        
        # Get column names from config file 
        # columns_to_multiply = [value for key, value in STOCK.__dict__.items() if not key.startswith('_')]
        columns_to_multiply = ['open', 'close', 'high', 'low']

        # Multiply columns pairwise
        for column in columns_to_multiply:
            merged_data = merged_data[f'{column}_stock'] * merged_data[f'{column}_fex']
        
        # Drop duplicated columns
        merged_data.drop(columns=[f'{column}_stock' for column in columns_to_multiply] + [f'{column}_fex' for column in columns_to_multiply], inplace=True)

        stock_data = merged_data

    return stock_data


# Get foreign exchange rate
def get_fex_rate_usd(to_currency: str, from_currency="USD") -> float:
    
    full_url = f"{BASE_URL}function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={AV_API_KEY}"

    r = requests.get(full_url)
    data = r.json()

    fex_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

    return float(fex_rate)

# Transform USD to new currency in stock data
def calc_new_currency(data: DataFrame, to_currency: str) -> DataFrame:
    exchange_rate_to_usd = get_fex_rate_usd(to_currency)
    data[[STOCK.OPEN, STOCK.HIGH, STOCK.LOW, STOCK.CLOSE]] *= exchange_rate_to_usd

    return data

