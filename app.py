import streamlit as st 
from av_api import get_timeseries, calc_timeseries_new_currency, filter_data_by_cutoff
from plot import plot_timeseries

from conf import DICT_STOCK_LABELS, STOCK, DICT_PERIOD_RANGE


def main():
    st.title("Alpha Vantage Stock Visualizer")

    st.sidebar.title("Options")

    # Dropdown menu for selecting stock
    selected_stock = st.sidebar.selectbox("Select a stock", list(DICT_STOCK_LABELS.values()), index=0)

    # Dropdown menu for selecting data type
    selected_data = st.sidebar.selectbox("Select data type", [STOCK.OPEN, STOCK.HIGH, STOCK.CLOSE, STOCK.LOW], index=2)

    # Dropdown menu for selecting periodicity
    selected_periodicity = st.sidebar.selectbox("Select periodicity", ["daily", "weekly", "monthly"], index=0)

    # Dropdown menu for selecting currency
    selected_currency = st.sidebar.selectbox("Select currency", ["USD", "EUR", "GBP", "CAD", "JPY", "CNY"], index=0)

  
    # Slider for selecting time range
    time_label, range_limits, default_value = DICT_PERIOD_RANGE[selected_periodicity]
    selected_time_range = st.sidebar.slider(f"Select time range ({time_label})", *range_limits, default_value)

    # Get timeseries data according to perdiodicity and time range
    if (selected_time_range > 100):
        outputsize = "full"
    else:
        outputsize = "compact"
    
    data = get_timeseries(selected_stock, selected_periodicity, outputsize=outputsize)

    data = filter_data_by_cutoff(data, n_cutoff=selected_time_range)
    
    # Calculate new currency if it is selected
    if selected_currency != "USD":
        data = calc_timeseries_new_currency(stock_data=data, to_currency=selected_currency)

    # Plot selected data against timestamp
    fig = plot_timeseries(data, selected_data, selected_stock, selected_periodicity, selected_currency)
    st.pyplot(fig)


if __name__ == "__main__":
    main()