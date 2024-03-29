import requests
from pandas import DataFrame, read_csv, merge
from io import StringIO
from alpha_vantage.timeseries import TimeSeries

from conf import AV_API_KEY, BASE_URL, STOCK, TIMESTAMP


# Functins to access stock data
def get_timeseries(stock_label: str, periodicity = "daily", outputsize="compact") -> DataFrame:
    
    if periodicity not in ["daily", "weekly", "monthly"]:
        print("No correct periodicity provided. Daily stock prices are used as default.")
        periodicity = "daily"
    
    # Get stock time series data
    full_url_stock = f"{BASE_URL}function=TIME_SERIES_{periodicity.upper()}&symbol={stock_label}&outputsize={outputsize}&apikey={AV_API_KEY}&datatype=csv"
    r = requests.get(full_url_stock).content
    stock_data = read_csv(StringIO(r.decode("utf-8")))

    print(stock_data.columns)

    # Ensure 'timestamp' column is present
    if TIMESTAMP not in stock_data.columns:
        raise KeyError("The 'timestamp' column is missing in the data.")
    
    return stock_data

# Filter data by cutoff date
def filter_data_by_cutoff(data, n_cutoff):
    # Calculate the max date from the timestamp column
    max_date = data[TIMESTAMP].max()
    
    # Calculate distinct dates sorted in descending order
    distinct_dates = sorted(data[TIMESTAMP].unique(), reverse=True)
    
    # Select the date at the position n_cutoff counting from last to first
    if n_cutoff <= len(distinct_dates):
        cutoff_date = distinct_dates[n_cutoff - 1]
    else:
        cutoff_date = distinct_dates[-1]
     
    return data[(data[TIMESTAMP] <= max_date) & (data[TIMESTAMP] >= cutoff_date)]

# Get foreign exchange rate
def get_fex_rate(to_currency: str, periodicity = "daily", outputsize="compact", from_currency="USD") -> DataFrame:
    if periodicity not in ["daily", "weekly", "monthly"]:
        print("No correct periodicity provided. Daily stock prices are used as default.")
        periodicity = "daily"
    
    full_url_fex_rate = f"{BASE_URL}function=FX_{periodicity.upper()}&from_symbol=USD&to_symbol={to_currency}&outputsize={outputsize}&apikey={AV_API_KEY}&datatype=csv"
    r = requests.get(full_url_fex_rate).content
    fex_data = read_csv(StringIO(r.decode("utf-8")))

    return fex_data


# Transform USD to new currency in time series
def calc_timeseries_new_currency(stock_data: DataFrame, to_currency: str) -> DataFrame:
        
        fex_data = get_fex_rate(to_currency=to_currency)

        # Merge the two dataframes on the 'timestamp' column
        merged_data = merge(stock_data, fex_data, on=TIMESTAMP, suffixes=("_stock", "_fex"))
        
        # Get column names from config file       
        columns_to_multiply = [ STOCK.OPEN, STOCK.CLOSE, STOCK.HIGH, STOCK.LOW ] 
        
        # Multiply columns pairwise
        for column in columns_to_multiply:
            merged_data[column] = merged_data[f'{column}_stock'] * merged_data[f'{column}_fex']
        
        merged_data[STOCK.VOL] = merged_data[f'{STOCK.VOL}_stock']

        return merged_data[[TIMESTAMP] + columns_to_multiply + [STOCK.VOL]]
