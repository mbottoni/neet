# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def run_check_root(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False

            if node1.val == node2.val:
                return True and run_check_root(node1.left, node2.left) and run_check_root(node1.right, node2.right)
            else:
                return False

        def run_tree(node):
            if node:
                if run_check_root(node, subRoot):
                    return True
                else:
                    return False or run_tree(node.left) or run_tree(node.right)
            return False

        return run_tree(root)
        
        