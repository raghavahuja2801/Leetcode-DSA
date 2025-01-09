def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

# Example usage
n = 5
k = 2
print(binomial_coefficient(n, k))  # Output: 10
