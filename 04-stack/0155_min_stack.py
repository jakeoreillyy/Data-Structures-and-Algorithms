"""
LeetCode 0155 · Min Stack  |  Stack  |  Medium
Time: O(1)  Space: O(n)

Problem:
    Design a stack that supports push, pop, top, and retrieving the minimum
    element, all in O(1) time.

Example:
    minStack.push(-2) → stack: [-2]
    minStack.push(0)  → stack: [-2, 0]
    minStack.push(-3) → stack: [-2, 0, -3]
    minStack.getMin() → -3
    minStack.pop()    → stack: [-2, 0]
    minStack.top()    → 0
    minStack.getMin() → -2

Idea:
    Maintain two stacks in sync: the main stack and a min stack.
    On every push, append the value to the main stack and append either
    the new value (if it's a new minimum) or the current minimum to the
    min stack. On every pop, remove from both. getMin() is then always
    a O(1) peek at the top of the min stack.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
