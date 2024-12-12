# Solution for 1389. Create Target Array in the Given Order

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/create-target-array-in-the-given-order/)

## Solution

```python
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(index)):
            ans.insert(index[i],nums[i])
        return ans
        