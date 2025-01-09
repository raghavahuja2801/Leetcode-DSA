def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
n = 5
print(factorial_recursive(n))  # Output: 120
