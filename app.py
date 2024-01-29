import streamlit as st 
from av_api import get_timeseries
from conf import DICT_STOCK_LABELS
from plot import plot_timeseries


def main():
    st.title("Alpha Vantage Stock Visualizer")

    st.sidebar.title("Options")

    # Dropdown menu for selecting stock
    selected_stock = st.sidebar.selectbox("Select a stock", list(DICT_STOCK_LABELS.keys()), index=0)

    # Dropdown menu for selecting data type
    selected_data = st.sidebar.selectbox("Select data type", ["open", "high", "close", "low"], index=2)

    # Dropdown menu for selecting periodicity
    selected_periodicity = st.sidebar.selectbox("Select periodicity", ["daily", "weekly", "monthly"], index=0)

    # Dropdown menu for selecting currency
    selected_currency = st.sidebar.selectbox("Select currency", ["USD", "EUR", "GBP", "CAD", "JPY", "CNY"], index=0)

    # Get time series data
    data = get_timeseries(selected_stock, periodicity=selected_periodicity)

    # Plot selected data against timestamp
    fig = plot_timeseries(data, selected_data, selected_stock, selected_periodicity, selected_currency)
    st.pyplot(fig)


if __name__ == "__main__":
    main()