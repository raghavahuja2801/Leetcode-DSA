# Solution for 69. Sqrt(x)

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/sqrtx/)

## Solution

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        low, high = 0,x
        while low<=high:
            mid = (low+high)/2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid +  1
            else:
                high = mid - 1
        return high