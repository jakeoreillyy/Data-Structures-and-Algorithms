"""
Remove Nth Node From End of List
Leetcode Problem: 19
Difficulty: Medium
Description: Given a linked list, remove the n-th node from the end of list and return its head. For example, Given linked list: 1->2->3->4->5, and n = 2, after removing the second node from the end, the linked list becomes 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head