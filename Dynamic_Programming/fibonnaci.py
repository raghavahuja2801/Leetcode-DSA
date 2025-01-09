# Memoization (Top-Down approach)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Tabulation (Bottom-Up approach)
def fibonacci_tab(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage
n = 10
print(f"Fibonacci of {n} (Memoization):", fibonacci_memo(n))
print(f"Fibonacci of {n} (Tabulation):", fibonacci_tab(n))
