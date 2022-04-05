from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def is_empty(self):
        return not self.__length

    def insert_first(self, value):
        first_node = Node(value)
        first_node.next = self.head_node
        self.head_node = first_node
        self.__length += 1

    def insert_last(self, value):
        last_node = Node(value)
        current_node = self.head_node

        if self.is_empty():
            return self.insert_first(value)

        while current_node.next:
            current_node = current_node.next
        current_node.next = last_node
        self.__length += 1
