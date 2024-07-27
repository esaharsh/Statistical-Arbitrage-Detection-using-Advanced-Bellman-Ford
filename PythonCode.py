import pandas as pd
import numpy as np
import time

file_path = '/kaggle/input/currency-exchange-rates/forex.csv'  # I have used this forex dataset on Kaggle
df = pd.read_csv(file_path)

#Print the Dataset
print("Dataset:")
print(df.head())

# Data Cleaning to avoid irregularities
df.dropna(inplace=True)
df['date'] = pd.to_datetime(df['date'])
df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].apply(pd.to_numeric)
df['base_currency'] = df['slug'].str.split('/').str[0]
df['quote_currency'] = df['slug'].str.split('/').str[1]

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

# Reducing the dataset size by sampling to avoid larger computation time
# You can change the fraction as per your convenience
sample_fraction = 0.1 
df_sampled = df.sample(frac=sample_fraction, random_state=1)

print(f"\nSampled {sample_fraction * 100}% of the data.")
print(df_sampled.head())

# I am using Bellman Ford Algorithm to find negative-cycles, which serve as profitable trades
def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph}
    predecessor = {node: None for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
                    predecessor[neighbor] = node

    # Checking for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                cycle = []
                current = neighbor
                while True:
                    cycle.append(current)
                    current = predecessor[current]
                    if current in cycle:
                        cycle.append(current)
                        cycle = cycle[cycle.index(current):]
                        return cycle
    return None

# Creating the graph from the dataset
def create_graph(df):
    graph = {}
    for _, row in df.iterrows():
        base = row['base_currency']
        quote = row['quote_currency']
        rate = row['close']
        if base not in graph:
            graph[base] = {}
        if quote not in graph:
            graph[quote] = {}
        graph[base][quote] = -np.log(rate)
        graph[quote][base] = np.log(rate)  # Add the reverse exchange rate for completeness
    return graph

# Measure the time taken to create the graph and printing it
start_time = time.time()
graph = create_graph(df_sampled)
print("\nTime taken to create the graph:", time.time() - start_time, "seconds")

# Measure the time taken to find arbitrage opportunity and printing it
start_time = time.time()
arbitrage_opportunity = bellman_ford(graph, list(graph.keys())[0])
print("\nTime taken to find arbitrage opportunity:", time.time() - start_time, "seconds")

if arbitrage_opportunity:
    print("\nArbitrage Opportunity Detected!")
    print("Route:", " -> ".join(arbitrage_opportunity))
else:
    print("\nNo Arbitrage Opportunity Detected")
