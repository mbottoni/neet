# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n_good = []
        def run_tree(node, path):
            if node:
                if  max(path) <= node.val:
                    n_good.append(True)
                run_tree(node.left, path+[node.val])
                run_tree(node.right, path+[node.val])

        run_tree(root, [-999999])
        return sum(n_good)
        