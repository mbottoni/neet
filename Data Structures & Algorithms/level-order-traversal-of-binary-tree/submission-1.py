# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(list)
        def run_tree(node,depth):
            if node:
                d[depth] = d[depth] + [node.val]
                run_tree(node.left, depth+1)
                run_tree(node.right, depth+1)
        run_tree(root,0)
        return list(d.values())
        