import matplotlib.pyplot as plt
from pandas import DataFrame

def plot_timeseries(data: DataFrame, selected_data: str, selected_stock: str, selected_periodicity: str, selected_currency: str) -> plt.Figure:
    # Sort data by timestamp in ascending order
    data.sort_values(by="timestamp", inplace=True)

    # Plot options
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data["timestamp"], data[selected_data], marker='o', linestyle='-')
    ax.set_title(f"{selected_stock} - {selected_data.capitalize()} Price ({selected_periodicity.capitalize()})")
    # ax.set_xlabel("Date")
    ax.set_ylabel(f"{selected_data.capitalize()} ({selected_currency})")
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xticks(rotation=45)

    return fig
