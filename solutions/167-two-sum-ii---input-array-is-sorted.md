# Solution for 167. Two Sum II - Input Array Is Sorted

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/search-insert-position/)

## Solution

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1  # 0-based index for left and right
    
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-based indices as per the problem statement
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1  # Move left pointer to the right to increase the sum
            else:
                right -= 1  # Move right pointer to the left to decrease the sum
