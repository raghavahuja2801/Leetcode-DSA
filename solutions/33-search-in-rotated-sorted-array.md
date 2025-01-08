# Solution for 33. Search in Rotated Sorted Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Determine if the left part is sorted
            if nums[left] <= nums[mid]:
                # Target lies within the sorted left part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1