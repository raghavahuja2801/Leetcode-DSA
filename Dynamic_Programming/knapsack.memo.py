def knapsack_memo(weights, values, capacity, index, memo={}):
    if index == 0 or capacity == 0:
        return 0
    if (index, capacity) in memo:
        return memo[(index, capacity)]

    if weights[index - 1] <= capacity:
        include = values[index - 1] + knapsack_memo(weights, values, capacity - weights[index - 1], index - 1, memo)
        exclude = knapsack_memo(weights, values, capacity, index - 1, memo)
        memo[(index, capacity)] = max(include, exclude)
    else:
        memo[(index, capacity)] = knapsack_memo(weights, values, capacity, index - 1, memo)

    return memo[(index, capacity)]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
n = len(weights)
print("Maximum value in Knapsack (Memoization):", knapsack_memo(weights, values, capacity, n))
