"""
LeetCode 0217 · Contains Duplicate  |  Arrays & Hashing  |  Easy
Time: O(n)  Space: O(n)

Problem:
    Given an integer array nums, return True if any value appears at least
    twice, and False if every element is distinct.

Example:
    Input:  nums = [1, 2, 3, 1]
    Output: True

Idea:
    Iterate through nums maintaining a seen set. For each number, check if
    it already exists in the set - O(1) lookup. If so, return True early.
    Otherwise add it and continue. Returns False only if no duplicate found.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
