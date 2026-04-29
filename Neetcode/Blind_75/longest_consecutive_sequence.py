"""
Longest Consecutive Sequence
Difficulty: Medium

Description:
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Args:
    nums (List[int]): An unsorted array of integers.

Returns:
    int: The length of the longest consecutive elements sequence.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        group = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in group:
                length = 0
                while i + length in group:
                    length += 1
                longest = max(length, longest)
        return longest
