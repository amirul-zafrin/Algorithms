from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        curr = [root]
        res = []

        while curr:
            node = curr.pop()
            if node:
                curr.append(node.right)
                curr.append(node)
                curr.append(node.left)
            else:
                if curr:
                    node = curr.pop()
                    res.append(node.val)

        return res
