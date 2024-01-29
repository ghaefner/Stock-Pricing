import streamlit as st 
from av_api import get_timeseries
from conf import DICT_STOCK_LABELS
import matplotlib.pyplot as plt


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
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data["timestamp"], data[selected_data], marker='o', linestyle='-')
    ax.set_title(f"{DICT_STOCK_LABELS[selected_stock]} - {selected_data.capitalize()} Price")
    ax.set_xlabel("Date")
    ax.set_ylabel(selected_data.capitalize())
    plt.xticks(rotation=45)
    st.pyplot(fig)


if __name__ == "__main__":
    main()