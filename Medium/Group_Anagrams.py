"""
Group Anagrams
Leetcode Problem: 49
Difficulty: Medium
Description: Given an array of strings, group anagrams together. i.e. ["eat", "tea", "tan", "ate", "nat", "bat"] groups to [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for words in strs:
            key = tuple(sorted(words))
            groups[key].append(words)
        return list(groups.values())