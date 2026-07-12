"""
LeetCode 0019 · Remove Nth Node From End of List |  Linked List  |  Medium
Time: O(n)  Space: O(1)

Problem:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Idea:
    Create dummy node at the start of the list.
    Set fast to be n + 1 steps ahead of slow.
    Increment fast and slow by one.
    Slow will be at the node before n, so set it's next, to n's next.
    Return dummy.next so it doesn't return the node added.
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
