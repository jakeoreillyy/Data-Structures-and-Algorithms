"""
Swap Nodes in Pairs
Leetcode Problem: 24
Difficulty: Medium
Description: Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed). e.g. Given 1->2->3->4, return 2->1->4->3
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current and current.next:
            after = current.next
            prev.next = after
            current.next = after.next
            after.next = current
            prev = current
            current = current.next
        
        head = dummy.next
        return head
        