# Solution for 1491. Average Salary Excluding the Minimum and Maximum Salary

## Problem Statement

[Leetcode Link](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

## Solution

```python
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary_sum = 0
        for i in range(1,len(salary)-1):
            salary_sum += salary[i]
        return (salary_sum/ (len(salary) -2))