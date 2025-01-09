def largest_sum_contiguous_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Parameters:
        arr (list[int]): The array of integers.
    
    Returns:
        int: The largest sum of a contiguous subarray.
    """
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Largest sum of contiguous subarray:", largest_sum_contiguous_subarray(arr))
