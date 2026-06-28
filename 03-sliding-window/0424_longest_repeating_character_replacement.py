"""
LeetCode 0424 · Longest Repeating Character Replacement |  Sliding Window  |  Medium
Time: O(n)  Space: O(1)

Problem:
    You are given a string s and an integer k.
    You can choose any character of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Idea:
    Create a map of the count of each character.
    Check to see if the current count is more than the previous max.
    Check to see if the current window size - the max frequency is larger than k.
    If so, decrement the count and increment l.
    Calculate the new longest.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        l = 0
        freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            freq = max(freq, count[s[r]])

            while (r - l + 1) - freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        return longest
