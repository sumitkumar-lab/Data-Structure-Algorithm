from Tree.tree import TreeNode, root

# Insert node
def insert(root, data):
    if root is None:
        return TreeNode(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)

        elif data > root.data:
            root.right = insert(root.right, data)

    return root

