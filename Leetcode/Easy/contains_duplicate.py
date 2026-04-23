"""
Contains Duplicate
Leetcode Problem: 217
Difficulty: Easy
Description: Return true if any value appears at least twice in the array, and false if every element is distinct. e.g. [1,2,3,1] returns true, [1,2,3] returns false
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = set()

        for num in nums:
            if num in table:
                return True
            table.add(num)
        return False
