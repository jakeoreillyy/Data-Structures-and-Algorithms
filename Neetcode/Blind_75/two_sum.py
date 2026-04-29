"""
Two Sum
Difficulty: Easy

Description:
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

Args:
    nums (List[int]): Array of integers.
    target (int): Target sum to find.

Returns:
    List[int]: Indices of the two numbers that add up to target.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in table:
                return [table[diff], index]
            table[num] = index
