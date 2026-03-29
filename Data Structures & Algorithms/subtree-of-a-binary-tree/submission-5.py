# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        all_equal = []
        def check_child(subRoot, node, equal):
            if subRoot and node:
                if subRoot.val == node.val:
                    equal.append(True)
                else:
                    equal.append(False)
                check_child(subRoot.left, node.left, equal)
                check_child(subRoot.right, node.right, equal)
            elif subRoot and not node:
                equal.append(False)
            elif not subRoot and node:
                equal.append(False)
            elif not subRoot and not node:
                equal.append(True)


        def run_tree(node):
            if node:
                equal = []
                if node.val == subRoot.val:
                    check_child(subRoot, node, equal)
                    all_equal.append(equal)

                run_tree(node.left)
                run_tree(node.right)

        run_tree(root)
        return any([all(equal) for equal in all_equal])
        