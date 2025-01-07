# Solution for 374. Guess Number Higher or Lower

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/guess-number-higher-or-lower/)

## Solution

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle number
            result = guess(mid)
            
            if result == 0:
                return mid  # Correct guess
            elif result == 1:
                left = mid + 1  # The picked number is higher, so we search in the upper half
            else:
                right = mid - 1 