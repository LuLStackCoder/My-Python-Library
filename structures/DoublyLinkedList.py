from .Deque import Deque
from .Node import DoubleNode

class DoublyLinkedList(Deque):
    """
    Implementation of an DoublyLinkedList.
    """
    def insert(self, index, item) -> object:
        if index < 0:
            raise IndexError("Negative index")
        if self.empty() or index == 0:
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
    
