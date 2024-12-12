# Solution for 59. Spiral Matrix II

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/spiral-matrix-ii/)

## Solution

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        val = 1
        loop = 0
        square = n**2
        while val<=square:
            for i in range(loop,n-loop):
                matrix[loop][i] = val
                val+= 1
                if val > square: 
                    break
            if val > square: 
                break
            for i in range(1+loop,n-loop):
                matrix[i][n-1-loop] = val
                val+= 1
                if val > square: 
                    break
            if val > square: 
                    break
            for i in range(n-2-loop,-1+loop,-1):
                matrix[n-1-loop][i] = val
                val+=1
                if val > square: 
                    break
            if val > square: 
                    break

            for i in range(n-2-loop,loop,-1):
                matrix[i][0+loop] = val
                val+=1
                if val > square: 
                    break
            loop += 1
            
        return matrix
