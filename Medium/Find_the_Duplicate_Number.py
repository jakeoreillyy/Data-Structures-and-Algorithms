"""
Find the Duplicate Number
LeetCode problem: 287
Difficulty: Medium
Description: Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive, there is only one repeated number in nums, return this repeated number. i.e. [1,3,4,2,2] returns 2
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}

        for i in nums:
            table[i] = table.get(i, 0) + 1

        for i, n in table.items():
            if n > 1:
                return i