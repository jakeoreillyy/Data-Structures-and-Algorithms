"""
Two Sum
LeetCode problem: 1
Difficulty: Easy
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. i.e. Given nums = [2, 7, 11, 15], target = 9, the output should be [0, 1] because nums[0] + nums[1] == 9.
"""

class Solution(object):
    def twoSum(self, nums, target):
        index = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in index:
                return [index[diff], i]
            index[n] = i