# stack implementation with array
class Stack:

    def __init__(self):
        self.stack = []

    # Checking whether the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Adding elements to stack
    def push(self, data):
        self.stack.append(data)

    # Removing last element from the stack
    def pop(self):
        if self.isEmpty():
            return ('Stack Empty!')
        return self.stack.pop()

    # Getting the top element form the stack
    def top(self):
        if self.isEmpty():
            return ('Stack Empty!')
        return self.stack[-1]



# stack implementation with linked list
class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode

    def pop(self):
        if (self.isEmpty()):
            return ('Stack Empty!')
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def top(self):
        if self.isEmpty():
            return ('Stack Empty!')
        return self.root.data