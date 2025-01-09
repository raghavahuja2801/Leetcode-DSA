def coin_change(coins, amount):
    """
    Find the minimum number of coins required to make the given amount.
    
    Parameters:
        coins (list[int]): List of available coin denominations.
        amount (int): The total amount to make.
    
    Returns:
        int: The minimum number of coins needed.
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0

    for coin in coins:
        if amount >= coin:
            coin_count += amount // coin
            amount %= coin

    return coin_count if amount == 0 else -1  # Return -1 if no solution is possible

# Example usage
coins = [1, 5, 10, 25]
amount = 30
print("Minimum coins:", coin_change(coins, amount))
