# binary_search.py

def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): The sorted list of elements to search.
        target (int): The element to search for.
        
    Returns:
        int: The index of the target element if found, else -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid to prevent overflow

        # Debug statements
        print(f"Searching between indexes {left} and {right}. Middle index: {mid}")

        if arr[mid] == target:
            print(f"Found target {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"Target {target} is greater than {arr[mid]}. Searching the right half.")
            left = mid + 1
        else:
            print(f"Target {target} is less than {arr[mid]}. Searching the left half.")
            right = mid - 1

    print(f"Target {target} not found in the array.")
    return -1

# Example usage:
if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11]
    target = 7
    result = binary_search(array, target)
    print("Result:", result)
