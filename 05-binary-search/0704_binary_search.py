"""
LeetCode 0704 · Binary Search |  Binary Search  |  Easy
Time: O(log n)  Space: O(1)

Problem:
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums. If target exists,
    then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Idea:
    Use binary searching to cut the array in half for each check.
    If the current mid point is larger than the target, set the right pointer to mid - 1.
    If the current mid point is smaller than the target, set the left pointer to mid + 1.
    Return the mid index if you found the target, or -1 if it was never found.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
