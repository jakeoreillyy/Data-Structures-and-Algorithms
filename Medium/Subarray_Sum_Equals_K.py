"""
Subarray Sum Equals K
Leetcode Problem: 560
Difficulty: Medium
Description: Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k. i.e. Given nums = [1,1,1], k = 2, return 2.
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = 0
        seen = {0 : 1}

        for n in nums:
            prefix += n
            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
        return count
