# Solution for 1773. Count Items Matching a Rule

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/count-items-matching-a-rule/)

## Solution

```python
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        val = 0
        if ruleKey == "color":
            val = 1
        elif ruleKey == "name":
            val = 2

        for i in range(len(items)):
            if items[i][val] == ruleValue:
                count+=1
        return count
        