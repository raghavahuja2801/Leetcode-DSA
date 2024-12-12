# Solution for 1672. Richest Customer Wealth

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/richest-customer-wealth/)

## Solution

```python
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            if sum > max:
                max = sum
        return max
        