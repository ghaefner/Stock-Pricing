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


# Labels for stock data
class STOCK:
    OPEN = "open"
    HIGH = "high"
    LOW = "low"
    CLOSE = "close"

# Periodicty to range dictionary
# Define mapping of periodicity to time range labels and ranges
DICT_PERIOD_RANGE = {
    "daily": ("days", (1, 365), 30),
    "weekly": ("weeks", (1, 156), 10),
    "monthly": ("months", (1, 120), 12)
}
