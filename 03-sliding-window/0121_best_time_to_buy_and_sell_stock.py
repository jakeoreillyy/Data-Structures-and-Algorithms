"""
LeetCode 0121 · Best Time to Buy and Sell Stock |  Sliding Window  |  Easy
Time: O(n)  Space: O(1)

Problem:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Idea:
    Use two pointers starting at the same place.
    Loop through the prices and see if rights is less than left. If so, update left to right.
    Otherwise calculate the profit at the current window and update the maximum if it's larger.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue
            profit = max(profit, prices[r] - prices[l])

        return profit
