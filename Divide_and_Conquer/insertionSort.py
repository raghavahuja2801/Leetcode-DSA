# insertion_sort.py

def insertion_sort(arr):
    """
    Performs Insertion Sort on a given array.
    
    Insertion Sort builds the sorted array one element at a time by repeatedly
    taking the next element from the unsorted portion and inserting it into the
    correct position within the sorted portion.

    Time Complexity:
    - Best case: O(n) (when the array is already sorted)
    - Worst case: O(n^2) (when the array is sorted in reverse order)
    - Average case: O(n^2)
    
    Space Complexity: O(1) (in-place sorting).
    
    Parameters:
        arr (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)  # Length of the array
    
    for i in range(1, n):
        # Store the current element to be compared
        key = arr[i]
        j = i - 1
        
        # Shift elements of the sorted portion to the right if they are greater than the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at its correct position
        arr[j + 1] = key
    
    return arr


if __name__ == "__main__":
    # Example usage
    print("Insertion Sort Example")
    example_array = [12, 11, 13, 5, 6]
    print("Original array:", example_array)
    sorted_array = insertion_sort(example_array)
    print("Sorted array:", sorted_array)
