"""
Contains Duplicate II
Leetcode Problem: 219
Difficulty: Easy
Description: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. i.e. Given nums = [1,2,3,1], k = 3, the output should be true because nums[0] == nums[3] and abs(0 - 3) <= 3.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        table = {}

        for i, n in enumerate(nums):
            if n in table and i - table[n] <= k:
                return True
            table[n] = i
        return False