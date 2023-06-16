
# Transaction Analysis Script
Brought to you by @Krypto-Kiddo and @Sassycular

This script performs analysis on a dataset of transactions and provides insights into patterns, clustering, and suspicious addresses. It utilizes machine learning techniques such as K-means clustering and dimensionality reduction with Principal Component Analysis (PCA).

## Prerequisites

- Python 3.x
- Required Python packages: pandas, numpy, sklearn

## Usage

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/transaction-analysis.git
   ```

2. Install the required Python packages:

   ```shell
   pip install pandas numpy scikit-learn
   ```

3. Prepare the dataset:

   - Ensure you have a CSV file named `transactions.csv` containing the transaction data in the current directory.

4. Run the script:

   ```shell
   python transaction_analysis.py
   ```

5. Analyze the output:

   - The script performs preprocessing, dimensionality reduction, clustering, and analysis on the dataset.
   - The results will be printed, including the cluster statistics and the receiver addresses from the smallest cluster.

## Additional Information

- The script preprocesses the dataset by scaling numeric features and encoding categorical features.
- Feature engineering is performed to derive additional features such as "time since the last transaction" and "transaction count".
- Principal Component Analysis (PCA) is used to reduce the dimensionality of the dataset to two components for visualization purposes.
- K-means clustering is applied to group the transactions into clusters.
- The script provides cluster statistics, including mean values for each feature in each cluster.
- The receiver addresses from the smallest cluster are displayed as potential suspicious addresses.

Certainly! Here's a suggested "Updates" section you can add to your README:

## Updates

**16 January 2023**
- Added network graph visualization: A network graph was implemented to visualize the transaction data, providing insights into the connections between signer and receiver account IDs. The graph showcases the relationships between accounts and highlights nodes with different colors based on the number of transactions. 
