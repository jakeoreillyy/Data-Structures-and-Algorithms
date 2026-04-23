"""
Power of Two
Leetcode Problem: 231
Difficulty: Easy
Description: Returns either True or False dependent on if the number is a power of 2
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Ensure the number is greater than 0, then use a bitwise AND to check
        # whether all binary digits are 1 (True) or if any are 0 (False)
        return n > 0 and not (n & (n - 1))