# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_data = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            if x <= self.getMin():
                self.min_stack.append(x)
        self.stack_data.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack_data[-1]:
            self.min_stack.pop()
        self.stack_data.pop()

    def top(self) -> int:
        return self.stack_data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
