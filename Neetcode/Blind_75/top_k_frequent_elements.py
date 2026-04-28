"""
Top K Frequent Elements
Difficulty: Medium
Description: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. i.e. Given nums = [1,1,1,2,2,3] and k = 2, the output should be [1,2] because the value 1 appears three times and the value 2 appears twice in the array.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            group[num] = group.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in group.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, 0,-1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result[:k]

        return None