#Implement and upload source code to github for: Queue.
#Implemented with same functionality (api/interface) as the ones from the book.
#output is provided at the bottom of code
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size  # Fixed-size array
        self.front_index = 0  # Points to the front of the queue
        self.rear_index = 0  # Points to the next available slot
        self.count = 0  # Number of elements in the queue

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("Queue overflow")
        self.queue[self.rear_index] = x
        self.rear_index = (self.rear_index + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        val = self.queue[self.front_index]
        self.front_index = (self.front_index + 1) % self.size
        self.count -= 1
        return val

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front_index]

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", end=" ")
            for i in range(self.count):
                print(self.queue[(self.front_index + i) % self.size], end=" ")
            print()

# Example usage
if __name__ == "__main__":
    queue = Queue(5)  # Create a queue of size 5
    print("Initial queue:")
    queue.print_queue()  # Queue is empty
    
    print("\nEnqueueing elements into the queue:")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()  # Queue: 10 20 30

    print("\nFront element:", queue.front())  # Output: Front element: 10

    print("\nDequeuing an element from the queue:")
    dequeued = queue.dequeue()
    print(f"Dequeued element: {dequeued}")  # Output: Dequeued element: 10
    queue.print_queue()  # Queue: 20 30

    print("\nIs the queue empty?", queue.is_empty())  # Output: False
    print("Is the queue full?", queue.is_full())  # Output: False

#output:
#Initial queue:
#Queue is empty

#Enqueueing elements into the queue:
#Queue: 10 20 30 

#Front element: 10

#Dequeuing an element from the queue:
#Dequeued element: 10
#Queue: 20 30 

#Is the queue empty? False
#Is the queue full? False
