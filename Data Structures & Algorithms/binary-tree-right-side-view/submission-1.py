# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        d = []
        def run_tree(node, depth):
            if node:
                if depth not in d:
                    s.append(node.val)
                    d.append(depth)
                run_tree(node.right, depth = depth + 1)
                run_tree(node.left, depth = depth + 1)

        run_tree(root, depth = 0)
        return s
        