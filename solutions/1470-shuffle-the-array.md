# Solution for 1470. Shuffle the Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/shuffle-the-array/)

## Solution

```python
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new = []
        for i in range(n):
            new.append(nums[i])
            new.append(nums[i+n])
        return new
        