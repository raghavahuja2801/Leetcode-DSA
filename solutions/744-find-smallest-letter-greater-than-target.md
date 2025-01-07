# Solution for 744. Find Smallest Letter Greater Than Target

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

## Solution

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
    
        # Binary search to find the smallest character greater than target
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] > target:
                right = mid - 1  # Search in the left half to find a smaller candidate
            else:
                left = mid + 1  # Search in the right half
        
        # After the binary search, `left` points to the smallest character greater than target
        # If no such character exists, `left` will be out of bounds and we return the first element
        return letters[left % len(letters)]