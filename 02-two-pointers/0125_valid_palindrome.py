"""
LeetCode 0125 · Valid Palindrome  |  Two Pointers  |  Easy
Time: O(n)  Space: O(n)

Problem:
    A phrase is a palindrome if, after converting all uppercase letters to
    lowercase and removing all non-alphanumeric characters, it reads the
    same forward and backward. Alphanumeric characters include letters and
    numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true # "amanaplanacanalpanama" is a palindrome.

Idea:
    Build a new string keeping only alphanumeric characters, converted to
    lowercase. Then compare this string to its reverse. If they match,
    it's a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join(c.lower() for c in s if c.isalnum())
        return pal == pal[::-1]