def generate_permutations(arr):
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]
    
    result = []
    backtrack(0)
    return result

# Example usage
arr = [1, 2, 3]
print(generate_permutations(arr))
