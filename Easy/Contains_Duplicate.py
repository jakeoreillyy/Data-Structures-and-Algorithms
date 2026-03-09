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
        table = {}

        for num in nums:
            table[num] = table.get(num, 0) + 1

        for num, count in table.items():
            if count > 1:
                return True

        return False

