def rod_cutting(prices, n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], prices[j] + dp[i - j - 1])
    
    return dp[n]

# Example usage
prices = [2, 5, 7, 8, 10, 13, 15, 17, 20]
n = 8
print("Maximum profit:", rod_cutting(prices, n))
