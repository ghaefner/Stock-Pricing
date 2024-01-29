import os

# Get API KEY
AV_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY').strip()

# Base url of alpha vantage
BASE_URL = 'https://www.alphavantage.co/query?'

# Dictionary with Stocks to track
DICT_STOCK_LABELS = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc."
}

