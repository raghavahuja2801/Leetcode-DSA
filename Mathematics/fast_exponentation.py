def fast_exponentiation(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result *= base
        base *= base
        exp //= 2
    return result

# Example usage
base = 2
exp = 10
print(fast_exponentiation(base, exp))  # Output: 1024
