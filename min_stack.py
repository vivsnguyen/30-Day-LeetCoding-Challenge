"""
Design a stack that supports push, pop, top, and 
retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
 

Hint #1  
Consider each node in the stack having a minimum value.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
        self.stack.append(x)
        self.min = min(self.stack)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        
        self.stack.pop()

        if self.stack:
            self.min = min(self.stack)

    def top(self) -> int:
        """
        Get the top element.
        """

        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()