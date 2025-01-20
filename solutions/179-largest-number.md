# Solution for 179. Largest Number

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/largest-number/)

## Solution

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings for comparison
        nums_str = list(map(str, nums))
        
        # Custom bubble sort to avoid imports
        for i in range(len(nums_str)):
            for j in range(len(nums_str) - 1 - i):
                # Compare concatenated results
                if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                    # Swap to maintain the correct order
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
        
        # Join sorted strings to form the largest number
        result = ''.join(nums_str)
        # Handle edge case where the result might be "000...0"
        return '0' if result[0] == '0' else result
