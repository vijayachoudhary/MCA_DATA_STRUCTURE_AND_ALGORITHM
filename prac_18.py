class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node in BST
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Inorder Traversal (Sorted Output in BST)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main Program
if __name__ == "__main__":
    root = None

    # Insert elements into BST
    elements = [50, 30, 70, 20, 40, 60, 80]

    for elem in elements:
        root = insert(root, elem)

    print("Inorder Traversal (Sorted):")
    inorder(root)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nPostorder Traversal:")
    postorder(root)