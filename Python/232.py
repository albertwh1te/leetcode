class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push_to_pop(self) -> None:
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)
        self.push_to_pop()

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.push_to_pop()
        result = self.pop_stack.pop()
        self.push_to_pop()
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        print(self.pop_stack, self.push_stack)
        return self.pop_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0


queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())