class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1  # Initial height of the node
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a key into the AVL Tree."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            return node  # No duplicates allowed

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Left heavy
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        # Right heavy
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        # Left-Right case
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # Right-Left case
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        """Deletes a key from the AVL Tree."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Balance the node if needed
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def search(self, key):
        """Searches for a key in the AVL Tree."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node is not None
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """Returns a list of nodes in in-order traversal."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node


# Testing the AVL Tree Implementation
avl = AVLTree()

# Insert nodes
for key in [20, 15, 25, 10, 5, 1, 17, 30, 35]:
    avl.insert(key)

# In-order traversal before deletion
inorder_before_delete = avl.inorder_traversal()

# Searching for nodes
search_17 = avl.search(17)  # Expected: True
search_100 = avl.search(100)  # Expected: False

# Deleting nodes
avl.delete(1)   # Deleting a leaf node
inorder_after_delete_1 = avl.inorder_traversal()

avl.delete(10)  # Deleting node with one child
inorder_after_delete_10 = avl.inorder_traversal()

avl.delete(20)  # Deleting node with two children
inorder_after_delete_20 = avl.inorder_traversal()

# Output the test results
print("Inorder Traversal Before Deletion:", inorder_before_delete)
print("Search for 17:", search_17)
print("Search for 100:", search_100)
print("Inorder Traversal After Deleting 1:", inorder_after_delete_1)
print("Inorder Traversal After Deleting 10:", inorder_after_delete_10)
print("Inorder Traversal After Deleting 20:", inorder_after_delete_20)
