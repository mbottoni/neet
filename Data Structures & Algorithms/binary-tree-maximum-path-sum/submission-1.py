# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def run_tree(node):
            if node:
                max_l = run_tree(node.left)
                max_r = run_tree(node.right)
                max_l = max(max_l, 0)
                max_r = max(max_r, 0)
                res[0] = max(res[0], node.val+max_l+max_r)
                return node.val+max(max_l, max_r)
            else:
                return 0
        
        run_tree(root)
        return res[0]

