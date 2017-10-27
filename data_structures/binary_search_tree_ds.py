class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val

    def __str__(self):
        return "To be implemented...."

    def get_children_count(self):
        count = 0
        if self.l_child:
            count += 1
        if self.r_child:
            count += 1
        return count

    def is_leaf(self):
        return self.get_children_count() == 0


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return "To be implemented...."

    def __len__(self):
        return self.size

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.size += 1
        else:
            current_node = self.root
            while True:
                if new_node.data <= current_node.data:
                    if current_node.l_child is None:
                        current_node.l_child = new_node
                        new_node.parent = current_node
                        self.size += 1
                        break
                    else:
                        current_node = current_node.l_child
                else:
                    if current_node.r_child is None:
                        current_node.r_child = new_node
                        new_node.parent = current_node
                        self.size += 1
                        break
                    else:
                        current_node = current_node.r_child

    def delete(self, value):
        del_node = self.lookup(value)
        if del_node is not None:
            if del_node.is_leaf():
                self.delete_leaf(del_node)
            else:
                if del_node.l_child is not None:
                    successor = del_node.l_child
                    while successor.r_child is not None:
                        successor = successor.r_child
                else:
                    successor = del_node.r_child
                    while successor.l_child is not None:
                        successor = successor.l_child

                del_node.data = successor.data
                self.delete_leaf(successor)
            self.size -= 1

    @staticmethod
    def delete_leaf(node):
        if node.is_leaf():
            if node.parent.l_child is node:
                node.parent.l_child = None
            else:
                node.parent.r_child = None
            del node
        else:
            raise ValueError('The node ' + str(node.data) + ' is not a leaf node')

    def lookup(self, value):
        current_node = self.root
        while True:
            if current_node.data == value:
                return current_node
            elif value < current_node.data:
                if current_node.l_child is None:
                    return None
                else:
                    current_node = current_node.l_child
            else:
                if current_node.r_child is None:
                    return None
                else:
                    current_node = current_node.r_child

    def pre_order_print(self, root):
        if root is not None:
            print root.data
            self.pre_order_print(root.l_child)
            self.pre_order_print(root.r_child)

    def in_order_print(self, root):
        if root is not None:
            self.in_order_print(root.l_child)
            print root.data
            self.in_order_print(root.r_child)

    def post_order_print(self, root):
        if root is not None:
            self.post_order_print(root.l_child)
            self.post_order_print(root.r_child)
            print root.data

