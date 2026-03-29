# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_depth(node):
            if node:
                return 1 + max(check_depth(node.left), check_depth(node.right))
            else:
                return 0

        cond = []

        def run_tree(node):
            if node:
                dr =  check_depth(node.right)
                dl =  check_depth(node.left)
                if abs(dl - dr)>1:
                    cond.append(False)
                else:
                    cond.append(True)

                run_tree(node.left)
                run_tree(node.right)

        run_tree(root)
        return all(cond)
        