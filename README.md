# Forex Arbitrage Detection using Bellman-Ford Algorithm

This project aims to detect arbitrage opportunities in forex trading using the Bellman-Ford algorithm. Arbitrage opportunities exist when a trader can exploit price differences between different markets or securities to make a profit without any risk.

## Dataset

The dataset used for this project is the Forex dataset from Kaggle. The dataset includes historical exchange rates for various currency pairs.

### File Path

/kaggle/input/currency-exchange-rates/forex.csv

## Prerequisites

To run the code, you need the following Python libraries:

- pandas
- numpy

You can install the required libraries using pip:

## Data Cleaning and Preparation
Loading the Dataset:
The dataset is loaded into a pandas DataFrame.

Cleaning the Dataset:
Remove rows with missing values.
Convert the date column to datetime format.
Ensure the columns 'open', 'high', 'low', and 'close' are numeric.
Extract base and quote currencies from the 'slug' column.

Sampling the Dataset:
To reduce computation time, a fraction of the dataset is sampled. You can adjust the sampling fraction as needed.

## Bellman-Ford Algorithm
The Bellman-Ford algorithm is used to find negative-weight cycles in the graph, which correspond to arbitrage opportunities.

## Steps
1) Create the Graph
2) Each currency pair is represented as an edge in the graph.
3) The weight of the edge is the negative logarithm of the exchange rate to handle the multiplicative nature of currency conversion rates.
4) Detect Arbitrage
5) Initialize the distance to all nodes as infinity except the source node.
6) Relax all edges for |V|-1 times, where V is the number of vertices.
7) Check for negative-weight cycles.
   
## Execution Time
The time taken to create the graph and find arbitrage opportunities is measured and printed.

## Results
The code will print whether an arbitrage opportunity was detected and display the route if found.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
