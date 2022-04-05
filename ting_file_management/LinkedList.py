from ting_file_management.Node import Node


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

    def remove_first(self):
        old_head = self.head_node
        self.head_node = self.head_node.next
        self.__length -= 1
        return old_head

    def remove_last(self):
        before_last_node = self.head_node

        while before_last_node.next.next:
            before_last_node = before_last_node.next
        removed_value = before_last_node.next
        before_last_node.next = None
        self.__length -= 1
        return removed_value

    def peek_at(self, position):
        node_to_find = self.head_node

        if 0 < position >= len(self) or position < 0:
            raise IndexError()

        if node_to_find:
            while position > 0 and node_to_find.next:
                node_to_find = node_to_find.next
                position -= 1
            if node_to_find:
                return node_to_find
        else:
            raise IndexError()
