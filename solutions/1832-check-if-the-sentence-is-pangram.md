# Solution for 1832. Check if the Sentence Is Pangram

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)

## Solution

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        print(len(set(sentence)))
        if len(set(sentence)) == 26:
            return True
        else:
            return False
        