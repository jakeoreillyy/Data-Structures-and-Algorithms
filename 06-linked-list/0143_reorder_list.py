"""
LeetCode 0143 · Reorder List |  Linked List  |  Medium
Time: O(n)  Space: O(1)

Problem:
    You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Idea:
    Create a slow and fast pointer to find the middle of the linked list.
    Reverse the second half of the list.
    Set a variable to the start and end of the list.
    Set the starts next to the end.
    Set the ends next to the temp front (starts next node before pointing to end).
    Move start and end to the temp of each.
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nxt = slow.next
        slow.next = None
        prev = None
        while nxt:
            temp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = temp

        front = head
        back = prev
        while back:
            temp_front = front.next
            temp_back = back.next
            front.next = back
            back.next = temp_front
            front = temp_front
            back = temp_back
