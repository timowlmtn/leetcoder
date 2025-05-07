class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """
    Calculate the maximum depth of a binary tree.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        int: The maximum depth of the binary tree.
    """
    if not root:
        return 0
    else:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    # Example usage
    # Constructing a binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    depth = max_depth(root)
    print(f"Maximum depth of the binary tree: {depth}")  # Output: 3
