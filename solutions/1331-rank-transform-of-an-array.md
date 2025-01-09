# Solution for 1331. Rank Transform of an Array

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/rank-transform-of-an-array/)

## Solution

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort the array and remove duplicates
        sorted_arr = sorted(set(arr))
        
        # Step 2: Assign ranks to the elements
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_arr)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]

      