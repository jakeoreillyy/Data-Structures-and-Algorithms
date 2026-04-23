"""
Two Sum
Difficulty: Easy
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. e.g. Given nums = [2,7,11,15], target = 9, return [0,1] because nums[0] + nums[1] == 9.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in table:
                return [table[diff], index]
            table[num] = index
