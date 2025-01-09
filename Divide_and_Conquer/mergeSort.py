# merge_sort.py

def merge_sort(arr):
    """
    Perform Merge Sort on a given array.
    
    Merge Sort is a divide-and-conquer algorithm that splits the array into smaller subarrays,
    sorts them, and merges them back together in sorted order.

    Time Complexity:
    - Best case: O(n log n)
    - Worst case: O(n log n)
    - Average case: O(n log n)
    
    Space Complexity: O(n) (requires additional space for merging).
    
    Parameters:
        arr (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.

    Parameters:
        left (list): The first sorted array.
        right (list): The second sorted array.
    
    Returns:
        list: The merged sorted array.
    """
    merged = []
    i = j = 0

    # Compare elements from both halves and add the smallest one to the merged array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


if __name__ == "__main__":
    # Example usage
    print("Merge Sort Example")
    example_array = [6, 3, 8, 5, 2, 7, 4, 1]
    print("Original array:", example_array)
    sorted_array = merge_sort(example_array)
    print("Sorted array:", sorted_array)
