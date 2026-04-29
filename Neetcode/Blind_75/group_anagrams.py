"""
Group Anagrams
Difficulty: Medium

Description:
    Given an array of strings strs, group the anagrams together. An anagram
    is a word formed by rearranging all letters of another word. The answer
    may be returned in any order.

Args:
    strs (List[str]): Array of strings to group.

Returns:
    List[List[str]]: Groups of strings where each group contains anagrams of each other.

Time Complexity:  O(n * m) — n strings each of max length m
Space Complexity: O(n * m)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
