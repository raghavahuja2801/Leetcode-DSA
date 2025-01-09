# Solution for 1200. Minimum Absolute Difference

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/minimum-absolute-difference/)

## Solution

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answers = []
        min_abs = float('inf')
        for i in range(len(arr)-1):
            absolute = abs(arr[i] - arr[i+1])
            if absolute < min_abs:
                min_abs = absolute
                answers = []
                answers.append([arr[i],arr[i+1]])
            elif absolute == min_abs:
                answers.append([arr[i],arr[i+1]])
        return answers