"""
LeetCode 0739 · Daily Temperatures  |  Stack  |  Medium
Time: O(n)  Space: O(n)

Problem:
    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have to wait after the ith day
    to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Idea:
    Use a monotonic stack, keeping track of temperatures in descending order.
    Check if the current temp is greater than the top one.
    Map the index of the top and delete it.
    calculate the days and store in a result array.
    Add the current index to the stack.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
