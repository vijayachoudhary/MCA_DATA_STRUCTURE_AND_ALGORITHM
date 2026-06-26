class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Get height of node
def height(node):
    if not node:
        return 0
    return node.height


# Get balance factor
def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)


# Right rotate (LL case)
def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


# Left rotate (RR case)
def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# Insert node into AVL tree
def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Get balance factor
    balance = get_balance(root)

    # LL Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # RR Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # LR Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Main Program
if __name__ == "__main__":
    root = None
    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        root = insert(root, v)

    print("Inorder Traversal of AVL Tree:")
    inorder(root)

    