# Solution for 81. Search in Rotated Sorted Array II

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Determine if the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False