# selection_sort.py

def selection_sort(arr):
    """
    Performs Selection Sort on a given array.
    
    Selection Sort is a sorting algorithm that divides the array into two parts:
    - A sorted subarray, which is built up from left to right.
    - The remaining unsorted subarray.
    
    The algorithm repeatedly selects the smallest (or largest, for descending order)
    element from the unsorted subarray and swaps it with the leftmost unsorted element.

    Time Complexity:
    - Best case: O(n^2)
    - Worst case: O(n^2)
    - Average case: O(n^2)
    
    Space Complexity: O(1) (in-place sorting).
    
    Parameters:
        arr (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)  # Length of the array

    for i in range(n):
        # Assume the first unsorted element is the smallest
        min_index = i
        for j in range(i + 1, n):
            # Update min_index if a smaller element is found
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found smallest element with the first unsorted element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


if __name__ == "__main__":
    # Example usage
    print("Selection Sort Example")
    example_array = [64, 25, 12, 22, 11]
    print("Original array:", example_array)
    sorted_array = selection_sort(example_array)
    print("Sorted array:", sorted_array)
