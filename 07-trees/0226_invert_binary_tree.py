"""
LeetCode 0226 · Invert Binary Tree |  Trees  |  Easy
Time: O(n)  Space: O(h)

Problem:
    Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Idea:
    Check to see if the root is empty.
    Recursively call left and right as the new roots.
    Swap left and right values.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        temp = root.right
        root.right = root.left
        root.left = temp

        return root
