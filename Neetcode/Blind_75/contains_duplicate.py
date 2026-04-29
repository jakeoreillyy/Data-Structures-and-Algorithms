"""
Contains Duplicate
Difficulty: Easy

Description:
    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.

Args:
    nums (List[int]): Integer array to check for duplicates.

Returns:
    bool: True if any value appears at least twice, False if all elements are distinct.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group = set()
        for num in nums:
            if num in group:
                return True
            group.add(num)
        return False
