# Definition for a binary tree node.
from typing import Optional, List
from unittest.mock import NonCallableMagicMock


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, lst = [], []
        lst.append(root)

        if not root:
            return []

        while len(lst) > 0:
            node = lst.pop()
            res.append(node.val)
            if node.right is not None:
                lst.append(node.right)
            if node.left is not None:
                lst.append(node.left)
        return res
