# RECURSION & SIMPLE BACKTRACKING CHEAT SHEET

from typing import List, Optional

# 1. Fibonacci Number
# Compute the nth Fibonacci number with memoization to avoid exponential time.


class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def helper(k: int) -> int:
            if k <= 1:
                return k
            if k not in memo:
                memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)


# 2. Same Tree
# Recursively check if two binary trees are structurally identical and have the same values.


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 3. Generate Parentheses
# Use backtracking to build all combinations of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def backtrack(curr: str, open_count: int, close_count: int):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res


# 4. Subsets
# Backtrack to generate all subsets (the power set) of a list of numbers.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(start: int, path: List[int]):
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# GENERAL TIPS
# • Always define clear base cases and memoize when subproblems overlap.
# • Outline your recursion/backtracking state (parameters, path) before coding.
# • Ensure you undo state changes (e.g., pop) after each recursive call.
# • Discuss time/space complexity: naive recursion/backtracking is often O(2^n), memoization can reduce to O(n).
# • Mention pruning strategies to skip unnecessary branches early.
