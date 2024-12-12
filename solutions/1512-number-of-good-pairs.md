# Solution for 1512. Number of Good Pairs

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/number-of-good-pairs/)

## Solution

```python
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if j == i :
                    continue
                if nums[i] == nums[j]:
                    count+=1
        return count