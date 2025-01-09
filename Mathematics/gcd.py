def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
a = 56
b = 98
print(gcd(a, b))  # Output: 14
