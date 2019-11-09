from .Deque import Deque
from .Node import DoubleNode

class DoublyLinkedList(Deque):
    """
    Implementation of an DoublyLinkedList.
    """
    def insert(self, index, item) -> object:
        if index < 0:
            raise IndexError("Negative index")
        elif self.empty() or index == 0:
            self.prepend(item)
        elif index >= self._size:
            self.append(item)
        else:
            temp = self._head
            for i in range(index):
                temp = temp.next
            new_node = DoubleNode(item, temp, temp.prev)
            temp.prev.next = new_node
            temp.prev = new_node
            self._size += 1
        return self

    def pop_at(self, index=0):
        if self.empty():
            raise IndexError("List empty")
        elif index < 0:
            raise IndexError("Negative index")
        if self._head is self._tail:
            del self._tail
            self._head = None
            self._tail = None
        elif index == 0:
            temp = self._head
            self._head = self._head.next
            self._head.prev = None
            del temp
        elif index >= self._size-1:
            temp = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            del temp
        else:
            temp = self._head
            for i in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            del temp
        self._size -= 1


    def remove(self, value):
        index = self.indexof(value)
        if index == -1:
            raise IndexError('No such value')
        else:
            self.pop_at(index)

    def clear(self) -> None:
        while not self.empty():
            self.pop()

    def reverse(self):
        temp = None
        curr = self._head
        tail = self._head
        head = self._tail
        while curr:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            curr = temp
        self._head = head
        self._tail = tail