# Solution for 1051. Height Checker

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/height-checker/)

## Solution

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        num = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                num += 1
        return num