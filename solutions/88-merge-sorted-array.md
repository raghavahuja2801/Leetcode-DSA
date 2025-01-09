# Solution for 88. Merge Sorted Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/merge-sorted-array/)

## Solution

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # Merge nums2 into nums1 starting from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Add remaining elements from nums2, if any
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1