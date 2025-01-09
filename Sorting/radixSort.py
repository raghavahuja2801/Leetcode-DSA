def counting_sort_for_radix(arr, exp):
    """
    A helper function to perform counting sort based on the digit at a specific place value.

    Parameters:
        arr (list[int]): The array to sort.
        exp (int): The digit place value to consider (1 for units, 10 for tens, etc.).
    
    Returns:
        list[int]: The partially sorted array based on the current digit.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # There are 10 possible digits (0-9)

    # Count occurrences of each digit in the current place value
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Modify count array to store cumulative frequencies
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):  # Process from the end for stable sorting
        index = (arr[i] // exp) % 10
        count[index] -= 1
        output[count[index]] = arr[i]

    return output

def radix_sort(arr):
    """
    Perform Radix Sort on the input array.
    
    Parameters:
        arr (list[int]): The array to sort.
    
    Returns:
        list[int]: The sorted array.
    """
    if not arr:
        return []

    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Perform counting sort for each digit (exp is 10^i where i is the digit place)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)
