def is_subset_sum(arr, n, target_sum):
    if target_sum == 0:
        return True
    if n == 0 and target_sum != 0:
        return False

    if arr[n - 1] > target_sum:
        return is_subset_sum(arr, n - 1, target_sum)

    return is_subset_sum(arr, n - 1, target_sum) or is_subset_sum(arr, n - 1, target_sum - arr[n - 1])

# Example usage
arr = [3, 34, 4, 12, 5, 2]
target_sum = 9
print(is_subset_sum(arr, len(arr), target_sum))  # Output: True
