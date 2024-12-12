# Solution for 1929. Concatenation of Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/concatenation-of-array/)

## Solution

```python
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans
        