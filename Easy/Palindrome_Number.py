"""
Palindrome Number
Leetcode Problem: 9
Difficulty: Easy
Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward. e.g. 121 is a palindrome while 123 is not.
"""

class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        return False 
        