"""
Tree: Is This a Binary Search Tree? - https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
Approach: Recursively check if the left child is less than the parent and the right child is greater than the parent.
Time complexity: O(n)
Space complexity: O(1)
"""

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def isBST(root, min_val, max_val):
    if root is None:
        return True

    if root.data <= min_val or root.data >= max_val:
        return False

    return isBST(root.left, min_val, root.data) and isBST(
        root.right, root.data, max_val
    )


def checkBST(root):
    return isBST(root, float("-inf"), float("inf"))
