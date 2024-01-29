from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame, read_csv
import io
from conf import AV_API_KEY, BASE_URL


# Functins to access stock data
def get_timeseries(stock_label: str, periodicity = "daily", API_KEY = AV_API_KEY) -> DataFrame:
    
    if periodicity not in ["daily", "weekly", "monthly"]:
        print("No correct periodicity provided. Daily stock prices are used as default.")
        periodicity = "daily"
    
    full_url = f"{BASE_URL}function=TIME_SERIES_{periodicity.upper()}&symbol={stock_label}&apikey={API_KEY}&datatype=csv"
    
    
    r = requests.get(full_url).content
    data = read_csv(io.StringIO(r.decode("utf-8")))

    return data



