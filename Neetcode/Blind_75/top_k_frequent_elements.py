"""
Top K Frequent Elements
Difficulty: Medium

Description:
    Given an integer array nums and an integer k, return the k most frequent
    elements. The answer may be returned in any order.

Args:
    nums (List[int]): Array of integers.
    k (int): Number of top frequent elements to return.

Returns:
    List[int]: The k most frequent elements.

Time Complexity:  O(n)
Space Complexity: O(n)
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
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result[:k]

        return None
