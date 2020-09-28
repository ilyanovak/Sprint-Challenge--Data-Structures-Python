class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, curr_node=None, prev=None):
        # while current node is not None
        while curr_node:
            # current node
            print(curr_node.value)
            # save current node's next node for next iteration
            next = curr_node.next_node
            # change order of current node
            curr_node.next_node = prev
            # change previous node for next iteration
            prev = curr_node
            # change current node for next iteration
            curr_node = next
        self.head = prev
