# quick_sort.py

def quick_sort(arr):
    """
    Perform QuickSort on a given array.
    
    QuickSort is a divide-and-conquer algorithm that partitions the array
    into two halves around a pivot such that all elements smaller than the pivot
    are on the left and all elements greater than the pivot are on the right.
    
    Time Complexity:
    - Best case: O(n log n)
    - Average case: O(n log n)
    - Worst case: O(n^2) (occurs when the pivot is the smallest or largest element)
    
    Space Complexity: O(log n) (for recursive call stack)

    Parameters:
        arr (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a pivot (we'll use the last element)
    pivot = arr[-1]
    left = []
    right = []

    # Step 2: Partition the array into left (<= pivot) and right (> pivot)
    for i in range(len(arr) - 1):  # Exclude the pivot
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Step 3: Recursively sort left and right, and combine
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    # Example usage
    print("QuickSort Example")
    example_array = [6, 3, 8, 5, 2, 7, 4, 1]
    print("Original array:", example_array)
    sorted_array = quick_sort(example_array)
    print("Sorted array:", sorted_array)
