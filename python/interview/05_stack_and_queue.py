# STACK & QUEUE CHEAT SHEET

from typing import List
from collections import deque


# 1. Valid Parentheses
# Use a stack to ensure each closing bracket matches the most recent opening.
class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            elif ch in mapping:
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                # ignore non-bracket characters if needed
                continue
        return not stack


# 2. Min Stack
# Support push, pop, top, and getMin in O(1) time by storing current min with each value.
class MinStack:
    def __init__(self):
        self.stack: List[tuple[int, int]] = []

    def push(self, x: int) -> None:
        current_min = x if not self.stack else min(x, self.stack[-1][1])
        self.stack.append((x, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else -1


# 3. Implement Queue using Stacks
# Use two stacks to simulate FIFO behavior.
class MyQueue:
    def __init__(self):
        self.in_stack: List[int] = []
        self.out_stack: List[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop() if self.out_stack else -1

    def peek(self) -> int:
        self._move()
        return self.out_sta_
