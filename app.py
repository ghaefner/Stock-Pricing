import streamlit as st 
from av_api import get_timeseries
from conf import DICT_STOCK_LABELS
from plot import plot_timeseries


def main():
    st.title("Alpha Vantage Stock Visualizer")

    # Dropdown menu for selecting stock
    selected_stock = st.selectbox("Select a stock", list(DICT_STOCK_LABELS.keys()), index=0)

    # Dropdown menu for selecting data type
    selected_data = st.selectbox("Select data type", ["open", "high", "close", "low"], index=2)

    # Dropdown menu for selecting periodicity
    selected_periodicity = st.selectbox("Select periodicity", ["daily", "weekly", "monthly"], index=0)

    # Get time series data
    data = get_timeseries(selected_stock, periodicity=selected_periodicity)

    # Plot selected data against timestamp
    fig = plot_timeseries(data, selected_data, selected_stock, selected_periodicity)
    st.pyplot(fig)


if __name__ == "__main__":
    main()