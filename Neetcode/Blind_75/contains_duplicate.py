"""
Contains Duplicate
Difficulty: Easy
Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. i.e. Given nums = [1,2,3,1], the output should be true because the value 1 appears twice in the array.
"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
