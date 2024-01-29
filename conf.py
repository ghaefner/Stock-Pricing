import os

# Get API KEY
AV_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY').strip()

# Dictionary with Stocks to track
DICT_STOCK_LABELS = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc."
}
