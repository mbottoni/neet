class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        x = [""]
        y = [""]
        def inorder(node):
            if node:
                inorder(node.left)
                x[0] = x[0] + str(node.val) + ","
                inorder(node.right)

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                y[0] = y[0] + str(node.val) + ","  # move append to end

        postorder(root)
        inorder(root)
        
        return str(x[0]) + "#" + str(y[0])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        inorder, postorder = data.split("#")
        inorder = [int(i) for i in inorder.split(',') if i != '']   # fix 1
        postorder = [int(i) for i in postorder.split(',') if i != ''] # fix 2

        def reconstruct_tree(inorder, postorder):
            if not inorder or not postorder:
                return None
            mid = len(inorder) - 1 - inorder[::-1].index(postorder[-1])  # search from right
            node = TreeNode(inorder[mid])
            node.left = reconstruct_tree(inorder[:mid], postorder[:mid])
            node.right = reconstruct_tree(inorder[mid+1:], postorder[mid:-1])
            return node
        return reconstruct_tree(inorder, postorder)