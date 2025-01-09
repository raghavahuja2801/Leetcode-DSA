# cycle_sort.py

def cycle_sort(arr):
    """
    Performs Cycle Sort on a given array.
    
    Cycle Sort minimizes the number of writes to the array by ensuring each
    element is written to its correct position exactly once.

    Time Complexity:
    - Best case: O(n^2)
    - Worst case: O(n^2)
    - Average case: O(n^2)
    
    Space Complexity: O(1) (in-place sorting).

    This algorithm is suitable for scenarios where minimizing the number of writes
    is important, such as in memory-constrained systems.

    Parameters:
        arr (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    
    # Loop through each element to find cycles
    for start in range(n - 1):
        item = arr[start]
        pos = start
        
        # Find the correct position of the current element
        for i in range(start + 1, n):
            if arr[i] < item:
                pos += 1
        
        # If the item is already in the correct position, skip it
        if pos == start:
            continue
        
        # Skip duplicates
        while pos < n and arr[pos] == item:
            pos += 1
        
        # Swap the current element with the correct position
        if pos != start:
            arr[pos], item = item, arr[pos]
        
        # Rotate the rest of the cycle
        while pos != start:
            pos = start
            for i in range(start + 1, n):
                if arr[i] < item:
                    pos += 1
            
            while pos < n and arr[pos] == item:
                pos += 1
            
            if pos != start:
                arr[pos], item = item, arr[pos]
    
    return arr


if __name__ == "__main__":
    # Example usage
    print("Cycle Sort Example")
    example_array = [4, 3, 2, 1]
    print("Original array:", example_array)
    sorted_array = cycle_sort(example_array)
    print("Sorted array:", sorted_array)
