# Solution for 1431. Kids With the Greatest Number of Candies

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

## Solution

```python
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        