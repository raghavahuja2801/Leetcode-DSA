# Solution for 34. Find First and Last Position of Element in Sorted Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Solution

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # Move left to find earlier occurrence
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1  # Move right to find later occurrence
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        first = findFirst(nums, target)
        if first == -1:
            return [-1, -1]  # Target not found
        last = findLast(nums, target)
        return [first, last]
```

---

## Approach

Since the array is sorted, we can use **binary search** to efficiently find the first and last occurrences of the target. Here’s the step-by-step approach:

1. **Find the First Occurrence**:
   - Use binary search to locate the smallest index `low` such that `nums[low] = target`.
   - To find earlier occurrences, move the `high` pointer left whenever the target is found.

2. **Find the Last Occurrence**:
   - Use binary search to locate the largest index `high` such that `nums[high] = target`.
   - To find later occurrences, move the `low` pointer right whenever the target is found.

3. **Return Result**:
   - If the first occurrence is not found (`first = -1`), return `[-1, -1]`.
   - Otherwise, return `[first, last]`.

---