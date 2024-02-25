import os

# Get API KEY
AV_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY').strip()

# Base url of alpha vantage
BASE_URL = 'https://www.alphavantage.co/query?'

# Timestamp column name
TIMESTAMP = "timestamp"

# Dictionary with Stocks to track
DICT_STOCK_LABELS = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "BNTX": "BioNTech SE",
    "AMZN": "Amazon.com, Inc.",
    "META": "Meta Platforms, Inc.",
    "TSLA": "Tesla, Inc.",
    "JPM": "JPMorgan Chase & Co.",
    "V": "Visa Inc.",
    "NVDA": "NVIDIA Corporation",
    "DIS": "The Walt Disney Company",
    "NFLX": "Netflix, Inc.",
    "CRM": "Salesforce.com, Inc.",
    "BRK-A": "Berkshire Hathaway Inc.",
    "PYPL": "PayPal Holdings, Inc.",
    "UNH": "UnitedHealth Group Incorporated",
    "HD": "The Home Depot, Inc.",
    "BAC": "Bank of America Corporation",
    "INTC": "Intel Corporation",
    "CSCO": "Cisco Systems, Inc."
}


# Labels for stock data
class STOCK:
    OPEN = "open"
    HIGH = "high"
    LOW = "low"
    CLOSE = "close"
    VOL = "volume"

# Periodicty to range dictionary
## Define mapping of periodicity to time range labels and ranges
DICT_PERIOD_RANGE = {
    "daily": ("days", (1, 365), 30),
    "weekly": ("weeks", (1, 156), 10),
    "monthly": ("months", (1, 120), 12)
}
