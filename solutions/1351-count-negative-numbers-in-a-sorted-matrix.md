# Solution for 1351. Count Negative Numbers in a Sorted Matrix

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

## Solution

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        row, col = 0, n - 1  # Start from top-right corner
        
        while row < m and col >= 0:
            if grid[row][col] < 0:
                # If the current element is negative, all elements below it in this column are negative
                count += (m - row)  # Count all negative numbers in the current column
                col -= 1  # Move left to check the next column
            else:
                row += 1  # Move down to the next row
        
        return count