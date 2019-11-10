from .AbstractLinkedList import AbstractLinkedList
from .Node import Node

class Queue(AbstractLinkedList):
    """
    Implementation of an Queue.
    """
    def __init__(self, iterable=None) -> None:
        super().__init__()
        if iterable != None:
            for i in iterable:
                self.enqueue(i)

    def enqueue(self, item) -> object:
        """
            Add an element to the tail.
        """
        new_node = Node(item)
        if (self.empty()):
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
        return self

    def dequeue(self):
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
        self._size -= 1
        return item

    def front(self):
        """
            Get a head value.
        """
        if not self.empty():
            return self._head.item
        else:
            raise IndexError(f"{self.__class__.__name__} empty")

    def back(self):
        """
            Get a tail value.
        """
        if not self.empty():
            return self._tail.item
        else:
            raise IndexError(f"{self.__class__.__name__} empty")

    def clear(self) -> None:
        """
            Remove all elements from the queue.
        """
        temp = self._head
        while not self.empty():
            self.dequeue()
