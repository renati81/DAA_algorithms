class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) >> 1

    def _left(self, index):
        return (index << 1) + 1

    def _right(self, index):
        return (index << 1) + 2

    def _heapify_down(self, index):
        left = self._left(index)
        right = self._right(index)
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def _heapify_up(self, index):
        parent = self._parent(index)
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def build_min_heap(self, array):
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        if len(self.heap) > 0:
            self._heapify_down(0)
        return root

    def peek(self):
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
    
    data = [5, 13, 2, 25, 7, 17, 20, 8, 4]

    min_heap = MinHeap()
    
    print("Building min heap with integers:")
    min_heap.build_min_heap(data)
    print(f"Heap after build: {min_heap}")

    print("\nAdding integer elements to heap:")
    min_heap.push(1)
    print(f"Heap after adding 1: {min_heap}")
    min_heap.push(9)
    print(f"Heap after adding 9: {min_heap}")

    
    print("\nPopping the integer root element:")
    min_val = min_heap.pop()
    print(f"Popped element (root): {min_val}")
    print(f"Heap after pop: {min_heap}")

    print("\nPeeking at the integer root element:")
    min_val = min_heap.peek()
    print(f"Root element: {min_val}")
    print(f"Heap after peek: {min_heap}")

    float_data = [5.5, 13.3, 2.2, 25.1, 7.7, 17.9]

    print("\nBuilding min heap with floats:")
    min_heap.build_min_heap(float_data)
    print(f"Heap after build with floats: {min_heap}")

    min_heap.push(1.1)
    print(f"Heap after adding 1.1: {min_heap}")
    min_heap.push(9.9)
    print(f"Heap after adding 9.9: {min_heap}")

    print("\nPopping the float root element:")
    float_val = min_heap.pop()
    print(f"Popped float element (root): {float_val}")
    print(f"Heap after pop: {min_heap}")

    tuple_data = [(5, "apple"), (13, "banana"), (2, "cherry"), (25, "date"), (7, "elderberry"), (17, "fig")]

    print("\nBuilding min heap with tuples:")
    min_heap.build_min_heap(tuple_data)
    print(f"Heap after build with tuples: {min_heap}")

    min_heap.push((1, "grape"))
    print(f"Heap after adding (1, 'grape'): {min_heap}")
    min_heap.push((9, "honeydew"))
    print(f"Heap after adding (9, 'honeydew'): {min_heap}")

    print("\nPopping the tuple root element:")
    tuple_val = min_heap.pop()
    print(f"Popped tuple element (root): {tuple_val}")
    print(f"Heap after pop: {min_heap}")

    print(f"\nHeap size: {min_heap.size()}")
    
    print(f"Is heap empty? {min_heap.is_empty()}")
