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

    def append(self, item) -> object:
        """
            Add an element to the tail.
        """
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
        """
            Add an element to the head.
        """
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
        """
            Insert an element to the index-position.
        """
        if index < 0:
            raise IndexError("Negative index")
        elif self.empty() or index == 0:
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
        """
            Remove an element from index-position.
        """
        if self.empty():
            raise IndexError(f"{self.__class__.__name__} empty")
        elif index < 0:
            raise IndexError("Negative index")
        if self._head is self._tail:
            del self._head
            self._head = None
            self._tail = None
        elif index == 0:
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

    def remove(self, value):
        """
            Remove the first occurrence of an element
            from the list with particular value.
        """
        index = self.indexof(value)
        if index == -1:
            raise IndexError('No such value')
        else:
            self.pop(index)

    def clear(self) -> None:
        """
            Remove all elements from the list.
        """
        while not self.empty():
            self.pop()
    
    def reverse(self):
        """
            Reverse the list.
        """
        curr = self._head
        tail = self._head
        next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self._head = prev
        self._tail = tail
