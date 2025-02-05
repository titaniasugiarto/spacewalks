import matplotlib.pyplot as plt
import pandas as pd


# Helper functions

def read_json_to_dataframe(input_file):
    print(f'Reading JSON file {input_file}...')

    eva_df = pd.read_json(input_file, convert_dates=['date'])  
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)

    return eva_df

def write_dataframe_to_csv(eva_df, output_file):
    print(f'Saving  to CSV file {output_file}...')
    eva_df.to_csv(output_file, index=False)

def plot_data_and_save(eva_df, graph_file):
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