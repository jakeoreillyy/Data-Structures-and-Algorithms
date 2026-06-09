"""
LeetCode 0242 · Valid Anagram  |  Arrays & Hashing  |  Easy
Time: O(n)  Space: O(n)

Problem:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Idea:
    Build a frequency map of each character in s and t, then compare.
    Equal maps means one is an anagram of the other.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
