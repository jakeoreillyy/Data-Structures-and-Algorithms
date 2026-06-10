"""
LeetCode 0347 · Top K Frequent Elements  |  Arrays & Hashing  |  Medium
Time: O(n)  Space: O(n)

Problem:
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.

Example 1:
    Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
    Output: [1,2]

Idea:
    Build a frequency count of each number using a hash map. 
    Create buckets indexed by frequency (size n+1, since max frequency is n).
    Place each number into its corresponding frequency bucket. 
    Then iterate buckets from highest frequency to lowest, collecting numbers until k elements are returned.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for n in range(len(freq) - 1, 0, -1):
            for i in freq[n]:
                res.append(i)
                if len(res) == k:
                    return res
