"""
LeetCode 0049 · Group Anagrams  |  Arrays & Hashing  |  Medium
Time: O(n)  Space: O(n)

Problem:
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Idea:
    For each word, build a frequency count of 26 letters. 
    Convert it to a tuple (lists can't be dict keys) and use it as the hash map key.
    Since anagrams have identical character frequencies, they produce the same tuple and get grouped under the same key.
"""

from collections import defaultdict 
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            table[tuple(count)].append(s)
        return list(table.values())
