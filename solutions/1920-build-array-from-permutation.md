# Solution for 1920. Build Array from Permutation

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/build-array-from-permutation/)

## Solution

```python
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        