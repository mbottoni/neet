# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = []
        def run_tree(node, depth):
            if node:
                run_tree(node.left, depth = depth+1)
                run_tree(node.right, depth = depth+1)
            else:
                depths.append(depth)

        run_tree(root, depth = 0)
        print(depths)
        return max(depths)

        