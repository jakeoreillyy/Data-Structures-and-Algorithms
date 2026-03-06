"""
Valid Anagram
Leetcode Problem: 242
Difficulty: Easy
Description: Determine if two strings are anagrams of each other. i.e. "anagram" and "nagaram" are anagrams, but "rat" and "car" are not.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(t) == Counter(s)