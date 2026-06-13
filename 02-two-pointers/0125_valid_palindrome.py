"""
LeetCode 0125 · Valid Palindrome  |  Two Pointers  |  Easy
Time: O(n)  Space: O(1)

Problem:
    A phrase is a palindrome if, after converting all uppercase letters to
    lowercase and removing all non-alphanumeric characters, it reads the
    same forward and backward. Alphanumeric characters include letters and
    numbers.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true # "amanaplanacanalpanama" is a palindrome.

Idea:
    Use two pointers starting at each end of the string,
    skipping over any non-alphanumeric characters.
    Compare the lowercase versions of the characters at each pointer -
    if they ever differ, it's not a palindrome.
    Move pointers inward until they meet. An alternate O(n) space approach
    (commented above) builds a filtered string and compares it to its reverse.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Idea 1 - Time: O(n), Space: O(n)
        # p = "".join(c.lower() for c in s if c.isalnum())
        # return p == p[::-1]

        # Idea 2 - Time: O(n), Space: O(1)
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
