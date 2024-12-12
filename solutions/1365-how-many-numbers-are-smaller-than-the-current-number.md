# Solution for 1365. How Many Numbers Are Smaller Than the Current Number

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

## Solution

```python
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])
        return result
        