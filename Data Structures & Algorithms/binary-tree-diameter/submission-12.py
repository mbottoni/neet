# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameters = []
        def max_dia(node):
            if node:
                return 1 + max(max_dia(node.left), max_dia(node.right))
            else:
                return 0


        def run_tree(node):
            if node:
                diam = max_dia(node.left) + max_dia(node.right)
                diameters.append( diam )
                run_tree(node.left)
                run_tree(node.right)

        run_tree(root)
        return max(diameters)
        