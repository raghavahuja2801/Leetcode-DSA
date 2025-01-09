# Solution for 217. Contains Duplicate

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/contains-duplicate/)

## Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False