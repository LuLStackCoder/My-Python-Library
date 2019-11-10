from .AbstractLinkedList import AbstractLinkedList
from .Node import Node

class Stack(AbstractLinkedList):
    """
    Implementation of an Stack.
    """
    def __init__(self, iterable=None) -> None:
        self._head = None
        self._size = 0
        if iterable != None:
            for i in iterable:
                self.push(i)

    def push(self, item) -> object:
        """
            Add an element to the head.
        """
        new_node = Node(item, self._head)
        self._head = new_node
        self._size += 1
        return self

    def pop(self):
        """
            Remove an element from the head.
        """
        if self.empty():
            raise IndexError(f"{self.__class__.__name__} empty")
        temp_node = self._head.next
        item = self._head.item
        del self._head
        self._head = temp_node
        self._size -= 1
        return item

    def peek(self):
        """
            Get a head item.
        """
        if not self.empty():
            return self._head.item
        else:
            raise IndexError(f"{self.__class__.__name__} empty")

    def clear(self) -> None:
        """
            Remove all elements from the stack.
        """
        temp = self._head
        while not self.empty():
            self.pop()
