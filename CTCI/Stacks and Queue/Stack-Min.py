# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop, and min should all operate in O(1) time

class Stack:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val):
    self.stack.append(val)

    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)
  
  def pop(self):
    self.stack.pop()
    self.minStack.pop()
  
  def getMin(self) -> int:
    return self.minStack[-1]
  
  def top(self) -> int:
    return self.stack[-1]

# Test
myStack = Stack()
myStack.push(4)
myStack.push(5)
myStack.push(3)
myStack.push(2)
print("Stack:", myStack.stack)
print("Min Stack:", myStack.minStack)
myStack.pop()
print("Stack:", myStack.stack)
print("Min Stack:", myStack.minStack)
myStack.pop()
print("Stack:", myStack.stack)
print("Min Stack:", myStack.minStack)