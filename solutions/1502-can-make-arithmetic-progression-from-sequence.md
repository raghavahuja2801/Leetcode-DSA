# Solution for 1502. Can Make Arithmetic Progression From Sequence

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)

## Solution

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        setdiff = arr[0] - arr[1]
        for i in range(1,len(arr)-1):
            diff = arr[i] - arr[i+1]
            if diff != setdiff:
                return False
        return True