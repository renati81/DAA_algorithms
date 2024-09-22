# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        # Parent index using bitwise manipulation
        return (index - 1) >> 1

    def _left(self, index):
        # Left child index using bitwise manipulation
        return (index << 1) + 1

    def _right(self, index):
        # Right child index using bitwise manipulation
        return (index << 1) + 2

    def _heapify_down(self, index):
        # Heapify down to maintain the heap property
        left = self._left(index)
        right = self._right(index)
        smallest = index
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            # Swap and continue heapifying
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def _heapify_up(self, index):
        # Heapify up to maintain the heap property
        parent = self._parent(index)
        if index > 0 and self.heap[index] < self.heap[parent]:
            # Swap and continue heapifying
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def build_min_heap(self, array):
        # Build the heap from an unordered array
        self.heap = array
        # Start heapifying from the last parent node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def push(self, item):
        # Add a new item and heapify up
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        # Remove and return the root (minimum element)
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        root = self.heap[0]
        # Move the last element to the root and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        # Get the minimum element without removing it
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)
if __name__ == "__main__":
    # Example heap data
    data = [5, 13, 2, 25, 7, 17, 20, 8, 4]

    # Initialize the heap
    min_heap = MinHeap()

    # Build the heap
    print("Building min heap:")
    min_heap.build_min_heap(data)
    print(f"Heap after build: {min_heap}")

    # Add elements
    print("\nAdding elements to heap:")
    min_heap.push(1)
    print(f"Heap after adding 1: {min_heap}")
    min_heap.push(9)
    print(f"Heap after adding 9: {min_heap}")

    # Pop the minimum element (root)
    print("\nPopping the root element:")
    min_val = min_heap.pop()
    print(f"Popped element(root element): {min_val}")
    print(f"Heap after pop: {min_heap}")

    # Peek at the root element
    print("\nPeeking at the root element:")
    min_val = min_heap.peek()
    print(f"Root element: {min_val}")
    print(f"Heap after peek: {min_heap}")

    # Heap size
    print(f"\nHeap size: {min_heap.size()}")

    # Check if heap is empty
    print(f"Is heap empty? {min_heap.is_empty()}")
