# Solution for 153. Find Minimum in Rotated Sorted Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # Compare mid with the rightmost element
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            else:
                # Minimum is in the left half or at mid
                right = mid

        # After the loop, left == right pointing to the minimum
        return nums[left]