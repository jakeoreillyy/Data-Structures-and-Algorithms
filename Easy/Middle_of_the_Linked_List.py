"""
Middle of the Linked List
Leetcode Problem: 876
Difficulty: Easy
Description: Returns the middle node of a singly linked list. i.e. [1,2,3,4,5] returns node 3
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow