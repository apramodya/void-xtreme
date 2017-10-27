class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            item = self.items[-1]
            return item
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
