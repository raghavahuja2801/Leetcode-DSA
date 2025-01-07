# Solution for 1539. Kth Missing Positive Number

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/kth-missing-positive-number/)

## Solution

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Start with the first missing number being 1 and initialize the previous number as 0
        prev = 0
        for num in arr:
            # Count how many numbers are missing between prev and num
            missing_count = num - prev - 1
            if missing_count >= k:
                # The kth missing number is between prev and num
                return prev + k
            # Update prev to the current num
            prev = num
            k -= missing_count
        
        # If not found in the array, then the kth missing number is beyond the last element in arr
        return prev + k