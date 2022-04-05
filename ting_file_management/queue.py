from ting_file_management.LinkedList import LinkedList


class Queue:
    def __init__(self):
        self._stack = LinkedList()

    def __len__(self):
        return len(self._stack)

    def enqueue(self, value):
        self._stack.insert_last(value)

    def dequeue(self):
        return self._stack.remove_first().value

    def search(self, index):
        try:
            return self._stack.peek_at(index).value
        except IndexError:
            raise IndexError

# queue = Queue()
# queue.enqueue(42)
# queue.enqueue(43)
# queue.enqueue(44)

# given = queue.dequeue()
