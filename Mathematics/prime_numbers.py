def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(limit + 1) if primes[i]]

# Example usage
limit = 30
print(sieve_of_eratosthenes(limit))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
