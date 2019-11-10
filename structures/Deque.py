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
        """
            Add an element to the tail.
        """
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
        """
            Add an element to the head.
        """
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
        """
            Remove an element from the head.
        """
        if self.empty():
            raise IndexError(f"{self.__class__.__name__} empty")
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
        """
            Remove an element from the tail.
        """
        if self.empty():
            raise IndexError(f"{self.__class__.__name__} empty")
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
        """
            Get a head item.
        """
        if not self.empty():
            return self._head.item
        else:
            raise IndexError(f"{self.__class__.__name__} empty")

    def back(self):
        """
            Get a tail item.
        """
        if not self.empty():
            return self._tail.item
        else:
            raise IndexError(f"{self.__class__.__name__} empty")

    def clear(self) -> None:
        """
            Remove all elements from the list.
        """
        while not self.empty():
            self.pop()
