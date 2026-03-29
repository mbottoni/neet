# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cond = []
        def run_tree(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return run_tree(node.left, left, node.val) and run_tree(node.right, node.val, right)

        return run_tree(root, -99999999, 999999999)
