# Solution for 976. Largest Perimeter Triangle

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/largest-perimeter-triangle/)

## Solution

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort(reverse=True)  # Sort in descending order
        for i in range(len(nums) - 2):
            # Check if the triangle inequality holds
            if nums[i] < nums[i + 1] + nums[i + 2]:
                val = (nums[i] + nums[i + 1] + nums[i + 2])
                return (val)
        return 0