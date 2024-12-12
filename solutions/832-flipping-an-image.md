# Solution for 832. Flipping an Image

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/flipping-an-image/)

## Solution

```python
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
