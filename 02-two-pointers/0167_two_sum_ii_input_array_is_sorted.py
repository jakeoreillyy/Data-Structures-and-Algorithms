"""
LeetCode 0167 · Two Sum II - Input Array Is Sorted  |  Two Pointers  |  Medium
Time: O(n)  Space: O(1)

Problem:
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2] # The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Idea:
    Use two pointers starting at each end of the array,
    Check to see if the current sum of left + right is less or greater than.
    If it is less than, increment left.
    If it is more than, decrement right.
    Return the indexes in 1 based indexing.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]
            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                return [l + 1, r + 1]
