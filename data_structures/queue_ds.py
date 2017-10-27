class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        s = " "
        for item in self.items:
            s += " " + str(item)
        return s

    def __getitem__(self, item):
        return item in self.items

    def enqueue(self, item):
        self.items.insert(0, item)
        self.size += 1

    def dequeue(self):
        if len(self.items) > 0:
            self.size -= 1
            return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None

    def clear(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return len(self.items) == 0
