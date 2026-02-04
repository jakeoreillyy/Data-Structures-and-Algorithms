"""
Partition List
Leetcode Problem: 86
Difficulty: Medium
Description: Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. e.g. Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        dummy1 = ListNode()
        dummy2 = ListNode()
        prev1 = dummy1
        prev2 = dummy2
        current = head

        while current:
            if current.val < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev2.next = None
        prev1.next = dummy2.next
        head = dummy1.next
        return head