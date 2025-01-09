def chocolate_distribution(arr, m):
    """
    Distribute chocolates among students such that the difference between max and min is minimized.
    
    Parameters:
        arr (list[int]): The array of chocolates in each packet.
        m (int): The number of students.
    
    Returns:
        int: The minimum difference between max and min chocolates.
    """
    if m > len(arr):
        return -1  # Not enough packets
    
    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff

# Example usage
arr = [12, 4, 7, 9, 2, 23, 25, 41, 40, 28, 40, 48, 43, 49]
m = 7
print("Minimum difference:", chocolate_distribution(arr, m))
