"""
Valid Palindrome
LeetCode problem: 125
Difficulty: Easy
Description: Determines if a given string is a palindrome, considering only alphanumeric characters and ignoring cases. i.e. "A man, a plan, a canal: Panama" becomes "amanaplanacanalpanama" which is a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())

        return s == s[::-1]