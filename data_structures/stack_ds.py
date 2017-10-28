class Stack:
    # Initialization
    def __init__(self):
        self.items = list()

    # Push item
    def push(self, item):
        self.items.append(item)

    # Pop item
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    # Get item from the frond end
    def peek(self):
        if len(self.items) > 0:
            item = self.items[-1]
            return item
        else:
            return None

    # Get the size of the stack
    def size(self):
        return len(self.items)

    # Check whether the stack is empty or not
    def is_empty(self):
        return len(self.items) == 0
