import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


class TestTreeNodeInOrder(unittest.TestCase):

    def test_2_simple(self):
        # Create a sample binary tree
        #         1
        #        / \
        #       2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        expected_result = [2, 1, 3]
        result = inorder_traversal(root)

        self.assertEqual(expected_result, result)
        print(result)

    def test_inorder_traversal(self):
        # Create a sample binary tree
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

        # Expected inorder traversal:
        expected_result = [4, 2, 5, 1, 3]

        # Call the function to test
        result = inorder_traversal(root)

        # Assert the result
        self.assertEqual(expected_result, result)
