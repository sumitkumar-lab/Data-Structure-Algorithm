class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode("R")

root.left = TreeNode("A")
root.right = TreeNode("B")

root.left.left = TreeNode("C")
root.left.right = TreeNode("D")

root.right.left = TreeNode("E")
root.right.right = TreeNode("F")

root.right.right.left = TreeNode("G")

# print(root.right.right.left.data)

def preOrderTraversal(root):
    if root is None:
        return -1
    print(root.data, end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def inOrderTraversal(root):
    if root is None:
        return -1
    inOrderTraversal(root.left)
    print(root.data, end=" ")
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return -1
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=" ")

preOrderTraversal(root)
print("\n")
inOrderTraversal(root)
print("\n")
postOrderTraversal(root)