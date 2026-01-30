"""
Reverse Linked List
LeetCode problem: 206
Difficulty: Easy
Description: Reverses a singly linked list. i.e. [1,2,3,4,5] becomes [5,4,3,2,1]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        before = None
        after = head

        while after:
            after = head.next
            head.next = before
            before = head
            head = after
        return before
        