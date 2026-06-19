"""
LeetCode 0011 · Container With Most Water  |  Two Pointers  |  Medium
Time: O(n)  Space: O(1)

Problem:
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    In this case, the max area of water (blue section) the container can contain is 49.

Idea:
    Use two pointers starting at each end of the array,
    calculate the distance and minimum height between the left and right value.
    Multiply them to get the total amount of water.
    If the total is greater than the most so far, set the new most.
    Check to see which was smaller of the two and move whichever was.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        most = 0

        while l < r:
            gap = r - l
            top = min(height[l], height[r])
            total = top * gap

            most = max(total, most)

            if top == height[l]:
                l += 1
            else:
                r -= 1

        return most
