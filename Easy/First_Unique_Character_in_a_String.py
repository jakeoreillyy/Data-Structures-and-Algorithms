"""
First Unique Character in a String
Leetcode Problem: 387
Difficulty: Easy
Description: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1. e.g. s = "leetcode" returns 0, s = "loveleetcode" returns 2
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}

        for i in s:
            table[i] = table.get(i, 0) + 1

        for i, n in enumerate(s):
            if table[n] == 1:
                return i
        return -1