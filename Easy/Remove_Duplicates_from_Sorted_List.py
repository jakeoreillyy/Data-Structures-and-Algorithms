"""
Remove Duplicates from Sorted List
LeetCode problem: 83
Difficulty: Easy
Description: Removes duplicates from a sorted linked list such that each element
             appears only once. i.e. [1,1,2] becomes [1,2]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head

        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        