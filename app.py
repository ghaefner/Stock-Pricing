import streamlit as st 
from av_api import get_timeseries, calc_timeseries_new_currency
from conf import DICT_STOCK_LABELS, STOCK
from plot import plot_timeseries
from datetime import datetime


def main():
    st.title("Alpha Vantage Stock Visualizer")

    st.sidebar.title("Options")

    # Dropdown menu for selecting stock
    selected_stock = st.sidebar.selectbox("Select a stock", list(DICT_STOCK_LABELS.keys()), index=0)

    # Dropdown menu for selecting data type
    selected_data = st.sidebar.selectbox("Select data type", [STOCK.OPEN, STOCK.HIGH, STOCK.CLOSE, STOCK.LOW], index=2)

    # Dropdown menu for selecting periodicity
    selected_periodicity = st.sidebar.selectbox("Select periodicity", ["daily", "weekly", "monthly"], index=0)

    # Dropdown menu for selecting currency
    selected_currency = st.sidebar.selectbox("Select currency", ["USD", "EUR", "GBP", "CAD", "JPY", "CNY"], index=0)

    # Get timeseries data
    data = get_timeseries(selected_stock, selected_periodicity)

    # Calculate new currency if it is selected
    if selected_currency != "USD":
        data = calc_timeseries_new_currency(stock_data=data, to_currency=selected_currency)
    

     # Slider for selecting time range
    selected_time_range = st.sidebar.slider("Select time range (months)", 1, 36, 12)
    

    # Plot selected data against timestamp
    fig = plot_timeseries(data, selected_data, selected_stock, selected_periodicity, selected_currency)
    st.pyplot(fig)


if __name__ == "__main__":
    main()