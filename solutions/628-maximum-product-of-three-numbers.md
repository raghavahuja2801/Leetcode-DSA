# Solution for 628. Maximum Product of Three Numbers

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/maximum-product-of-three-numbers/)

## Solution

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # Product of the three largest numbers
        max_product1 = nums[-1] * nums[-2] * nums[-3]
        # Product of the two smallest numbers and the largest number
        max_product2 = nums[0] * nums[1] * nums[-1]
        return max(max_product1, max_product2)