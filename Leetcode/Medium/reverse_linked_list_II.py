"""
Reverse Linked List II
Leetcode Problem: 92
Difficulty: Medium
Description: Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list. e.g. Given 1->2->3->4->5, left = 2 and right = 4, return 1->4->3->2->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head <= 1:
            return
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range(left-1):
            prev = prev.next

        current = prev.next

        for i in range(right - left):
            move = current.next
            current.next = move.next
            move.next = prev.next
            prev.next = move

        head = dummy.next
        return head