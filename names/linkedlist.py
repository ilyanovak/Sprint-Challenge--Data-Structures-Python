class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def get_tail(self):
        if self.tail == None:
            return None
        else:
            return self.tail.get_value()

    def get_head(self):
        if self.head == None:
            return None
        else:
            return self.head.get_value()

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1
