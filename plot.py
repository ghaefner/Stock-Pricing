import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pandas import DataFrame

from conf import DICT_STOCK_LABELS

def plot_timeseries(data: DataFrame, selected_data: str, selected_stock: str, selected_periodicity: str, selected_currency: str) -> plt.Figure:
    # Sort data by timestamp in ascending order
    data.sort_values(by="timestamp", inplace=True)

    # Plot options
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data["timestamp"], data[selected_data], marker='o', linestyle='-')
    ax.set_title(f"{DICT_STOCK_LABELS[selected_stock]} - {selected_data.capitalize()} Price ({selected_periodicity.capitalize()})")
    
    # Set axes labels
    ax.set_ylabel(f"{DICT_STOCK_LABELS[selected_stock].capitalize()} ({selected_currency})")

    # Format y-axis tick labels to include dot for thousands
    formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x).replace(',', '.'))
    ax.yaxis.set_major_formatter(formatter)
    # Adjust y-axis limits
    min_value = data[selected_data].min() * 0.95
    max_value = data[selected_data].max() * 1.05
    ax.set_ylim(min_value, max_value)

    # Format x-acis tick labels
    ax.xaxis.set_major_locator(plt.MaxNLocator(12))
    plt.xticks(rotation=45)

    # Add grid
    ax.grid(True)

    return fig
