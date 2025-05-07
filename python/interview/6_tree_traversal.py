# TREE TRAVERSALS (BINARY TREES) CHEAT SHEET

from typing import List, Optional
from collections import deque


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


# 1. Maximum Depth of Binary Tree
# Use DFS (recursion) to compute the height of the tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 2. Symmetric Tree
# Check if a tree is a mirror of itself using DFS recursion.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isMirror(p.left, q.right) and isMirror(p.right, q.left)

        return isMirror(root, root)


# 3. Binary Tree Level Order Traversal
# Use BFS with a queue to traverse level by level.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res: List[List[int]] = []
        q = deque([root])
        while q:
            level_size = len(q)
            level: List[int] = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


# 4. Invert Binary Tree
# Swap left and right children recursively (DFS).
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# GENERAL TIPS
# • Confirm TreeNode definition is provided.
# • Clarify if recursion depth is safe or iterative is needed.
# • Choose DFS vs BFS based on problem (depth vs level operations).
# • State time/space: O(n) time, O(n) space for queue or recursion call stack.
# • Always test edge cases: empty tree, single node.
