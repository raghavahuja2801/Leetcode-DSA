def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Modular inverse doesn't exist if gcd is not 1
    return x % m

# Example usage
a = 3
m = 11
print(mod_inverse(a, m))  # Output: 4
