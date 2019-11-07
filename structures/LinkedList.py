from .AbstractLinkedList import AbstractLinkedList
from .Node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an LinkedList.
    """
    def __init__(self, iterable=None) -> None:
        super().__init__()
        if iterable != None:
            for i in iterable:
                self.append(i)

    def front(self):
        if not self.empty():
            return self._head.item
        else:
            raise IndexError("List empty")

    def back(self):
        if not self.empty():
            return self._tail.item
        else:
            raise IndexError("List empty")

    def append(self, item) -> object:
        new_node = Node(item)
        if self._head == None:
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
        return self

    def prepend(self, item) -> object:
        new_node = Node(item)
        if self._head == None:
            self._head = new_node
            self._tail = self._head
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1
        return self

    def insert(self, index, item) -> object:
        if index < 0:
            raise IndexError("Negative index")
        if self.empty() or index == 0:
            self.prepend(item)
        elif index >= self._size:
            self.append(item)
        else:
            temp = self._head
            for i in range(index-1):
                temp = temp.next
            new_node = Node(item, temp.next)
            temp.next = new_node
            self._size += 1
        return self

    def pop(self, index=0) -> None:
        if self.empty():
            raise IndexError("List empty")
        if index < 0:
            raise IndexError("Negative index")
        if index == 0:
            temp = self._head
            self._head = self._head.next
            del temp
        elif index >= self._size-1:
            temp = self._head
            while temp.next is not self._tail:
                temp = temp.next
            del self._tail
            self._tail = temp
            self._tail.next = None
        else:
            temp = self._head
            for i in range(index-1):
                temp = temp.next
            next_node = temp.next.next
            del temp.next
            temp.next = next_node
        self._size -= 1

    def clear(self) -> None:
        while not self.empty():
            self.pop()
