import matplotlib.pyplot as plt
import pandas as pd


# Helper functions

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas DataFrame.
    Clean the data while removing incomplete rows and sorting by date.

    Args:
        input_file (str): The path to the JSON file.

    Returns:
        eva_df (pd.DataFrame): The cleaned and sorted DataFrame.
    """
    print(f'Reading JSON file {input_file}...')

    eva_df = pd.read_json(input_file, convert_dates=['date'])  
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)

    return eva_df

def write_dataframe_to_csv(eva_df, output_file):
    """
    Write the DataFrame to a CSV file.

    Args:
        eva_df (pd.DataFrame): The DataFrame to be written into CSV file.
        output_file (str): The path to the CSV file.

    Returns:
        None, CSV file is automatically saved.

    """
    print(f'Saving  to CSV file {output_file}...')
    eva_df.to_csv(output_file, index=False)

def plot_data_and_save(eva_df, graph_file):
    """
    Calculate the cumulative time spent in space to date, plot, and save the data.

    Args:
        eva_df (pd.DataFrame): The DataFrame containing the EVA data.
        graph_file (str): The path to save the graph.
    
    Returns:
        None, the graph is automatically saved and displayed.
    
    """
    eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
    plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

# Main code

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='utf-8')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'


# Read the JSON file into a DataFrame
eva_df = read_json_to_dataframe(input_file)

# Convert the DataFrame to a CSV file
write_dataframe_to_csv(eva_df, output_file)

# Plot the cumulative time spent in space to date
plot_data_and_save(eva_df, graph_file)