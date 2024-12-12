# Solution for 1480. Running Sum of 1d Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/running-sum-of-1d-array/)

## Solution

```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for i in range(len(nums)):
            sum = 0
            for i in range(i+1):
                sum += nums[i]
            sums.append(sum)
        return sums
        