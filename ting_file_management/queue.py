from ting_file_management.LinkedList import LinkedList


class Queue:
    def __init__(self):
        self._stack = LinkedList()

    def __len__(self):
        return len(self._stack)

    def __iter__(self):
        return QueueIterator(self._stack)

    def enqueue(self, value):
        self._stack.insert_last(value)

    def dequeue(self):
        return self._stack.remove_first().value

    def search(self, index):
        try:
            return self._stack.peek_at(index).value
        except IndexError:
            raise IndexError

    def is_file_in_queue(self, file_name):
        current_node = self._stack.head_node
        position = 0
        if len(self) <= 0:
            return False

        while position <= len(self):
            if current_node.value['nome_do_arquivo'] == file_name:
                return True
            else:
                current_node = current_node.next
                position += 1
        return False


class QueueIterator():
    def __init__(self, stack):
        self.current_file = stack.head_node

    def __next__(self):
        if not self.current_file:
            raise StopIteration()

        file = self.current_file.value
        self.current_file = self.current_file.next
        return file
