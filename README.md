# Alpha Vantage Stock Visualizer

## Introduction
This Streamlit application allows users to visualize stock data obtained from the Alpha Vantage API. Users can select a stock from a predefined list and choose to visualize its open, high, close, or low prices over time.

## Installation
1. Clone this repository to your local machine:
git clone 

2. Navigate to the project directory

3. If necessary, install a virtual environment.

4. Install the required dependencies:
pip install -r requirements.txt

## Usage
1. Ensure you have set up the required environment variable `ALPHAVANTAGE_API_KEY` containing your Alpha Vantage API key.

2. Run the Streamlit application using the following command:
streamlit run app.py


3. The application will open in your default web browser. Select a stock from the dropdown menu and choose the type of data (open, high, close, or low) you want to visualize.

4. The plot will update dynamically based on your selections, showing the selected data against the timestamp.

## Environment Variable
- `ALPHAVANTAGE_API_KEY`: Your Alpha Vantage API key. Obtain it from the Alpha Vantage website and set it as an environment variable in your system.

## Modules
- `app.py`: Contains the Streamlit application code.
- `av_api.py`: Contains the function `get_timeseries` for fetching stock data from the Alpha Vantage API.



