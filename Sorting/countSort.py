def counting_sort(arr):
    """
    Perform Counting Sort on the input array.
    
    Parameters:
        arr (list[int]): The array to sort.
    
    Returns:
        list[int]: The sorted array.
    """
    if not arr:
        return []

    # Find the range of the input array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize the count array
    count = [0] * range_of_elements

    # Count the frequency of each element
    for num in arr:
        count[num - min_val] += 1

    # Modify count array to store cumulative frequencies
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
