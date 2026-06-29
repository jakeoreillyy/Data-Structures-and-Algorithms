"""
LeetCode 0020 · Valid Parentheses |  Stack  |  Easy
Time: O(n)  Space: O(n)

Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "([])"
    Output: true

Example 2:
    Input: s = "([)]"
    Output: false

Idea:
    Create a map of closing & opening bracket pairs.
    For each character: if it's a closing bracket, check if the top of
    the stack holds its matching opener - pop if so, else return False.
    Otherwise, append the opening bracket to the stack.
    Return True only if the stack is empty at the end.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
