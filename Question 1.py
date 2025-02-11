import numpy as np
import pandas as pd


def binomial_price_tree(S0, u, d, n):
    """
    Constructs a binomial price tree.

    Parameters:
    S0 (float): Initial stock price
    u (float): Upward movement factor
    d (float): Downward movement factor
    n (int): Number of time steps

    Returns:
    DataFrame: A DataFrame representing the binomial tree.
    """
    # Create an empty array to store stock prices
    tree = np.zeros((n + 1, n + 1))

    # Populate the binomial tree
    for i in range(n + 1):  # Time steps
        for j in range(i + 1):  # Nodes at each step
            tree[j, i] = S0 * (u ** (i - j)) * (d ** j)

    # Convert to DataFrame for better visualization
    df = pd.DataFrame(tree)
    df.index.name = "Node"
    df.columns.name = "Time Step"


    return df


# Example usage:
S0 = 100  # Initial stock price
u = 1.1  # Up-factor (10% increase)
d = 0.9  # Down-factor (10% decrease)
n = 10  # Number of time steps


df=binomial_price_tree(S0, u, d, n)
print(df)