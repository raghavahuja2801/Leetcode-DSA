def fractional_knapsack(weights, values, capacity):
    """
    Solve the Fractional Knapsack problem.
    
    Parameters:
        weights (list[int]): List of weights of items.
        values (list[int]): List of values of items.
        capacity (int): Capacity of the knapsack.
    
    Returns:
        float: Maximum value in the knapsack.
    """
    n = len(weights)
    items = [(values[i], weights[i], i) for i in range(n)]

    # Sort items by value/weight ratio
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    max_value = 0.0
    for value, weight, index in items:
        if capacity >= weight:
            capacity -= weight
            max_value += value
        else:
            max_value += value * (capacity / weight)
            break

    return max_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in knapsack:", fractional_knapsack(weights, values, capacity))
