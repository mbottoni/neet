# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def run_tree(node):
            if node:
                if node.left:
                    run_tree(node.left)
                if node.right:
                    run_tree(node.right)
                tmp = node.left
                node.left = node.right
                node.right = tmp


        run_tree(root)
        return root
        