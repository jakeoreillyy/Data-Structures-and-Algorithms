"""
LeetCode 0053 · Find Minimum in Rotated Sorted Array |  Binary Search  |  Medium
Time: O(log n)  Space: O(1)

Problem:
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
    1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Idea:
    Binary search while tracking the smallest value seen so far.
    If nums[l] < nums[r], the window is already sorted, so nums[l] is its minimum.
    Otherwise compare nums[mid] to nums[l]: if nums[mid] >= nums[l],
    the left half is sorted ascending and the minimum must be to the right (l = mid + 1);
    otherwise the minimum is at or before mid (r = mid).
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return res
