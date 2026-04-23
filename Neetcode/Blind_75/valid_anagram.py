"""
Valid Anagram
Difficulty: Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise. e.g. "anagram" and "nagaram" are anagrams, while "rat" and "car" are not.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)