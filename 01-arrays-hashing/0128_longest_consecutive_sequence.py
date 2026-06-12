"""
LeetCode 0128 · Longest Consecutive Sequence  |  Arrays & Hashing  |  Medium
Time: O(n)  Space: O(n)

Problem:
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4 # Sequence is [1, 2, 3, 4]. Therefore its length is 4.

Idea:
    Convert nums to a set for O(1) lookups.
    For each number, only start counting if it's the start of a sequence (i.e. n-1 is not in the set).
    From there, count forward while consecutive values exist, and track the longest length found.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0

        for n in unique:
            if n - 1 not in unique:
                length = 0
                while n + length in unique:
                    length += 1
                longest = max(longest, length)
        return longest
