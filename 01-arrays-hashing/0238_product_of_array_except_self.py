"""
LeetCode 0238 · Product of Array Except Self  |  Arrays & Hashing  |  Medium
Time: O(n)  Space: O(1)

Problem:
    Given an integer array nums, return an array answer such that answer[i]
    is equal to the product of all the elements of nums except nums[i].

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Idea:
    Iterate left to right, storing in res[i] the running product of all elements before index i (the prefix).
    Then iterate right to left, multiplying each res[i] by the running product of all elements after index i (the suffix).
    Combining prefix and suffix products gives the product of everything except nums[i], without ever dividing.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
