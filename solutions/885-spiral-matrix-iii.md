# Solution for 885. Spiral Matrix III

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/spiral-matrix-iii/)

## Solution

```python
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        # Directions: right (0), down (1), left (2), up (3)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        visited = set()
        
        r, c = rStart, cStart
        result.append([r, c])
        visited.add((r, c))
        
        steps = 1  # Number of steps to take in a given direction
        while len(result) < rows * cols:
            for d in range(4):  # Go through all directions (right, down, left, up)
                for _ in range(steps):
                    # Move in the current direction
                    r += directions[d][0]
                    c += directions[d][1]
                    
                    # Check if the current cell is within bounds and not visited
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        result.append([r, c])
                        visited.add((r, c))
                    
                    # If we've visited all cells, return the result
                    if len(result) == rows * cols:
                        return result
                
                # After right and left directions, increase the step count
                if d == 1 or d == 3:
                    steps += 1
        
        return result