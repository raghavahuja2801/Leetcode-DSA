# Solution for 268. Missing Number

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/missing-number/)

## Solution

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        val = sum(nums)
        lists = list(range(n))
        check = sum(lists)
        return check - val