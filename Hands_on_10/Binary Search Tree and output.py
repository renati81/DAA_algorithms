# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root is not None
        elif key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)
        return root

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, root, result):
        if root:
            result.append(root.key)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, root, result):
        if root:
            self._postorder_recursive(root.left, result)
            self._postorder_recursive(root.right, result)
            result.append(root.key)

# Testing the Binary Search Tree implementation
bst = BinarySearchTree()

# Insert nodes
for key in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(key)

# Traversals after insertion
inorder = bst.inorder_traversal()
preorder = bst.preorder_traversal()
postorder = bst.postorder_traversal()

# Search for nodes
search_50 = bst.search(50)  # Expected: True
search_25 = bst.search(25)  # Expected: False

# Delete a node
bst.delete(20)  # Delete leaf node
delete_leaf_inorder = bst.inorder_traversal()

bst.delete(30)  # Delete node with one child
delete_one_child_inorder = bst.inorder_traversal()

bst.delete(50)  # Delete node with two children
delete_two_children_inorder = bst.inorder_traversal()

# Output the test results
print("Inorder Traversal:", inorder)
print("Preorder Traversal:", preorder)
print("Postorder Traversal:", postorder)
print("Search for 50:", search_50)
print("Search for 25:", search_25)
print("Inorder after deleting 20:", delete_leaf_inorder)
print("Inorder after deleting 30:", delete_one_child_inorder)
print("Inorder after deleting 50:", delete_two_children_inorder)
