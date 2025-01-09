# bubble_sort.py

def bubble_sort(arr):
    """
    Performs Bubble Sort on a given array.
    
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. 
    The pass through the list is repeated until the list is sorted.

    Time Complexity:
    - Best case: O(n) when the array is already sorted (optimized version).
    - Worst case: O(n^2) when the array is reverse sorted.
    - Average case: O(n^2).
    
    Space Complexity: O(1) (in-place sorting).
    
    Parameters:
        arr (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """

    n = len(arr)  # Length of the array
    for i in range(n):
        # Flag to check if any swapping occurred in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the last pass, the array is already sorted
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    # Example usage
    print("Bubble Sort Example")
    example_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", example_array)
    sorted_array = bubble_sort(example_array)
    print("Sorted array:", sorted_array)
