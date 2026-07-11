"""
LeetCode 0206 · Reverse Linked List |  Linked List  |  Easy
Time: O(n)  Space: O(1)

Problem:
    Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Idea:
    While current is still in the list.
    Create a temporary variable nxt and set it to curr's next node.
    curr's next pointer goes to prev.
    prev gets updated to curr.
    curr goes to nxt.
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
