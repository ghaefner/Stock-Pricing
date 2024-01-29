from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame, read_csv
import io
from conf import AV_API_KEY, BASE_URL


# Functins to access stock data
def get_timeseries(stock_label: str, periodicity = "daily") -> DataFrame:
    
    if periodicity not in ["daily", "weekly", "monthly"]:
        print("No correct periodicity provided. Daily stock prices are used as default.")
        periodicity = "daily"
    
    full_url = f"{BASE_URL}function=TIME_SERIES_{periodicity.upper()}&symbol={stock_label}&apikey={AV_API_KEY}&datatype=csv"
    
    
    r = requests.get(full_url).content
    data = read_csv(io.StringIO(r.decode("utf-8")))

    return data


# Get foreign exchange rate
def get_fex_rate_usd(to_currency: str, from_currency="USD") -> float:
    
    full_url = f"{BASE_URL}function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={AV_API_KEY}"

    r = requests.get(full_url)
    data = r.json()

    return (data['Realtime Currency Exchange Rate'])['5. Exchange Rate']

