#Implement and upload source code to github for: stack.
#Implemented with same functionality (api/interface) as the ones from the book.
#output is provided at the bottom of code
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size  # Fixed-size array
        self.top_index = -1  # Top of the stack is initially -1 (empty)

    def push(self, x):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self.top_index += 1
        self.stack[self.top_index] = x

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        val = self.stack[self.top_index]
        self.top_index -= 1
        return val

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.size - 1

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top_index]

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:", self.stack[:self.top_index + 1])

# Example usage
if __name__ == "__main__":
    stack = Stack(5)  # Create a stack of size 5
    print("Initial stack:")
    stack.print_stack()  # Stack is empty
    
    print("\nPushing elements onto the stack:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()  # Stack: [10, 20, 30]

    print("\nTop element:", stack.top())  # Output: Top element: 30

    print("\nPopping an element from the stack:")
    popped = stack.pop()
    print(f"Popped element: {popped}")  # Output: Popped element: 30
    stack.print_stack()  # Stack: [10, 20]

    print("\nIs the stack empty?", stack.is_empty())  # Output: False
    print("Is the stack full?", stack.is_full())  # Output: False

#output:
#Initial stack:
#Stack is empty

#Pushing elements onto the stack:
#Stack: [10, 20, 30]

#Top element: 30

#Popping an element from the stack:
#Popped element: 30
#Stack: [10, 20]

#Is the stack empty? False
#Is the stack full? False
