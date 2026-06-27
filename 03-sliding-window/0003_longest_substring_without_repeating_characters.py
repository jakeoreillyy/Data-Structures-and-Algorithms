"""
LeetCode 0003 · Longest Substring Without Repeating Characters |  Sliding Window  |  Medium
Time: O(n)  Space: O(n)

Problem:
    Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Idea:
    Use two pointers starting at the same place.
    Loop through the string and see if the right character is in the set.
    If so, remove left from seen and update left until it is gone.
    Add the right character to the set.
    Calculate max vs current.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest