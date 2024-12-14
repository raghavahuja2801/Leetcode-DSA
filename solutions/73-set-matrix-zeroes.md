# Solution for 73. Set Matrix Zeroes

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/set-matrix-zeroes)

## Solution

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows_to_update = []
        cols_to_update = []
        
        for i in range(len(matrix)):
            for j in  range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows_to_update.append(i)
                    cols_to_update.append(j)
 
        for i in rows_to_update:
            matrix[i] = [0] * len(matrix[i])
        
        for j in cols_to_update:
            for i in range(len(matrix)):
                matrix[i][j] = 0



