class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s = ""
        p = self.head
        while p is not None:
            s += str(p.data) + ' '
            p = p.next
        return s + "| size: " + str(self.size)

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        return False        # Not implemented yet

    def insert(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_to_end(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def search(self, value):
        p = self.head
        while p is not None:
            if p.data == value:
                return p
            p = p.next

    def delete(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                self.size -= 1
            current_node = current_node.next
