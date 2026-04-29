"""
Valid Anagram
Difficulty: Easy

Description:
    Given two strings s and t, return true if t is an anagram of s, and
    false otherwise. An anagram uses all original letters exactly once.

Args:
    s (str): The source string.
    t (str): The string to check against s.

Returns:
    bool: True if t is an anagram of s, False otherwise.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
