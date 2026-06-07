"""
LeetCode 0001 · Two Sum  |  Arrays & Hashing  |  Easy
Time: O(n)  Space: O(n)

Problem:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Each input has exactly one solution and you may not use the same element twice.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] # nums[0] + nums[1] == 9

Idea:
    Store each number's index in a hash map as we iterate. For each number, check if the difference (target - num) is already in the map.
    If so, we've found the pair in a single pass.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in table:
                return [table[diff], i]
            table[num] = i
