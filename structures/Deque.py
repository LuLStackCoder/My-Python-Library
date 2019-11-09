from .AbstractLinkedList import AbstractLinkedList
from .Node import DoubleNode

class Deque(AbstractLinkedList):
    """
    Implementation of an Deque.
    """
    def __init__(self, iterable=None) -> None:
        super().__init__()
        if iterable != None:
            for i in iterable:
                self.append(i)
    
    def append(self, item) -> object:
        new_node = DoubleNode(item, None, self._tail)
        if (self.empty()):
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
        return self

    def prepend(self, item) -> object:
        new_node = DoubleNode(item, self._head, None)
        if (self.empty()):
            self._head = new_node
            self._tail = self._head
        else:
            self._head.prev = new_node
            self._head = new_node
        self._size += 1
        return self

    def shift(self):
        if self.empty():
            raise IndexError("Deque empty")
        item = self._head.item
        if self._head is self._tail:
            del self._head
            self._head = None
            self._tail = None
        else:
            temp_node = self._head.next
            del self._head
            self._head = temp_node
            self._head.prev = None
        self._size -= 1
        return item

    def pop(self):
        if self.empty():
            raise IndexError("Deque empty")
        item = self._tail.item
        if self._head is self._tail:
            del self._tail
            self._head = None
            self._tail = None
        else:
            temp_node = self._tail.prev
            del self._tail
            self._tail = temp_node
            self._tail.next = None
        self._size -= 1
        return item

    def front(self):
        if not self.empty():
            return self._head.item
        else:
            raise IndexError("Deque empty")

    def back(self):
        if not self.empty():
            return self._tail.item
        else:
            raise IndexError("Deque empty")

    def clear(self) -> None:
        while not self.empty():
            self.pop()
