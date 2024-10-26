class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"  # New nodes are always red
        
class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL
        
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
                
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
            
        self.fix_insert(node)
        
    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"
        
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
        
    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
        
    def maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node
        
    def delete(self, key):
        z = self.search(key)
        if z:
            self._delete_node(z)
            
    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
                
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == "BLACK":
            self.fix_delete(x)
            
    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    # Query Operations
    def search(self, key):
        """Search for a key in the tree"""
        return self._search_recursive(self.root, key)
        
    def _search_recursive(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def range_query(self, low, high):
        """Find all keys in the range [low, high]"""
        result = []
        self._range_query_recursive(self.root, low, high, result)
        return result
    
    def _range_query_recursive(self, node, low, high, result):
        if node == self.NIL:
            return
        
        if low < node.key:
            self._range_query_recursive(node.left, low, high, result)
            
        if low <= node.key <= high:
            result.append(node.key)
            
        if high > node.key:
            self._range_query_recursive(node.right, low, high, result)

    def find_predecessor(self, key):
        """Find the predecessor of a given key"""
        node = self.search(key)
        if node == self.NIL:
            return None
            
        if node.left != self.NIL:
            return self.maximum(node.left).key
            
        y = node.parent
        while y != None and node == y.left:
            node = y
            y = y.parent
        return y.key if y else None

    def find_successor(self, key):
        """Find the successor of a given key"""
        node = self.search(key)
        if node == self.NIL:
            return None
            
        if node.right != self.NIL:
            return self.minimum(node.right).key
            
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        return y.key if y else None

    def find_min(self):
        """Find the minimum key in the tree"""
        if self.root == self.NIL:
            return None
        return self.minimum(self.root).key

    def find_max(self):
        """Find the maximum key in the tree"""
        if self.root == self.NIL:
            return None
        return self.maximum(self.root).key

    def count_nodes(self):
        """Count total nodes in the tree"""
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        if node == self.NIL:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    def height(self):
        """Calculate the height of the tree"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node == self.NIL:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))
        
    def inorder(self):
        """Inorder traversal of the tree"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
        
    def _inorder_recursive(self, node, result):
        if node != self.NIL:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
            
    def is_valid_rb_tree(self):
        """Verify if the tree maintains Red-Black properties"""
        if self.root.color != "BLACK":
            return False
        
        black_height = [0]
        return self._is_valid_rb_tree_recursive(self.root, black_height)
        
    def _is_valid_rb_tree_recursive(self, node, black_height):
        if node == self.NIL:
            return True
            
        if node.color != "RED" and node.color != "BLACK":
            return False
            
        if node.color == "RED":
            if (node.left != self.NIL and node.left.color == "RED") or \
               (node.right != self.NIL and node.right.color == "RED"):
                return False
                
        left_height = [0]
        right_height = [0]
        
        if not self._is_valid_rb_tree_recursive(node.left, left_height):
            return False
        if not self._is_valid_rb_tree_recursive(node.right, right_height):
            return False
            
        black_height[0] = left_height[0] + (1 if node.color == "BLACK" else 0)
        
        if left_height[0] != right_height[0]:
            return False
            
        return True

def test_red_black_tree():
    """Comprehensive test suite for Red-Black Tree"""
    # Test 1: Basic insertion and search
    print("Test 1: Basic insertion and search")
    tree = RedBlackTree()
    test_values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    
    for value in test_values:
        tree.insert(value)
        print(f"Inserted {value}")
    
    print("Inorder traversal:", tree.inorder())
    print("Is valid RB tree?", tree.is_valid_rb_tree())
    
    # Test 2: Query operations
    print("\nTest 2: Query operations")
    print("Tree height:", tree.height())
    print("Total nodes:", tree.count_nodes())
    print("Minimum value:", tree.find_min())
    print("Maximum value:", tree.find_max())
    print("Predecessor of 10:", tree.find_predecessor(10))
    print("Successor of 10:", tree.find_successor(10))
    print("Range query [5, 15]:", tree.range_query(5, 15))
    
    # Test 3: Search operations
    print("\nTest 3: Search operations")
    for value in [8, 11, 15]:
        result = tree.search(value)
        print(f"Searching for {value}: {'Found' if result != tree.NIL else 'Not found'}")
    
    # Test 4: Deletion
    print("\nTest 4: Deletion")
    delete_values = [18, 11, 3]
    for value in delete_values:
        print(f"Deleting {value}")
        tree.delete(value)
        print("Inorder traversal after deletion:", tree.inorder())
        print("Is valid RB tree?", tree.is_valid_rb_tree())
        print("Tree height after deletion:", tree.height())
        print("Total nodes after deletion:", tree.count_nodes())
    
    # Test 5: Stress test with more operations
    print("\nTest 5: Stress test")
    stress_values = [15, 17, 19, 21, 23]
    for value in stress_values:
        tree.insert(value)
    print("Inorder traversal after stress insertions:", tree.inorder())
    print("Range query [15, 22]:", tree.range_query(15, 22))
    print("Is valid RB tree?", tree.is_valid_rb_tree())
    
    # Test 6: Edge cases
    print("\nTest 6: Edge cases")
    empty_tree = RedBlackTree()
    print("Empty tree height:", empty_tree.height())
    print("Empty tree node count:", empty_tree.count_nodes())
    print("Empty tree min:", empty_tree.find_min())
    print("Empty tree max:", empty_tree.find_max())
    print("Empty tree range query [1, 10]:", empty_tree.range_query(1, 10))

if __name__ == "__main__":
    test_red_black_tree()
