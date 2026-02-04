"""
Linked List Convert Binary Number in a Linked List to Integer
Leetcode Problem: 1290
Difficulty: Easy
Description: Return the decimal value of the binary number represented by the linked list. e.g. [1,0,1] returns 5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current = head
        num = 0
        while current is not None:
            num = num * 2 + current.val
            current = current.next
        return num
        