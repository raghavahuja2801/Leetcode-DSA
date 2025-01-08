# Solution for 1608. Special Array With X Elements Greater Than or Equal X

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)

## Solution

```python
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            x = n - i  # Potential x value
            # Check if x satisfies the conditions
            if nums[i] >= x and (i == 0 or nums[i-1] < x):
                return x
                
        return -1  