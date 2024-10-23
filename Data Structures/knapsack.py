def knapsack(weights, values, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The last cell contains the maximum value

# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_value = knapsack(weights, values, capacity)
    print("Maximum value in knapsack:", max_value)
