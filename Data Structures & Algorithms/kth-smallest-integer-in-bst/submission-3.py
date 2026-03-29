# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def run_tree(node):
            if node:
                run_tree(node.left)
                arr.append(node.val)
                run_tree(node.right)

        run_tree(root)
        return arr[k-1]

        