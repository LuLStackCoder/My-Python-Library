from .Queue import Queue
from .Node import PQNode

class PriorityQueue(Queue):
    """
    Implementation of an Priority Queue.
    """
    def enqueue(self, item, priority: int=None) -> object:
        """
            Add an element with priority, or 
            if there is no priority, the integer element
            has priority equal to its value.
        """
        if priority is None:
            if isinstance(item, int):
                priority = item
            else:
                raise TypeError("Item without priority must be integer")
        if not isinstance(priority, int) or priority <= 0:
            raise TypeError("Priority must be positive integer")
        if self.empty():
            self._head = PQNode(item, priority)
            self._tail = self._head
        elif self._head.priority < priority:
            self._head = PQNode(item, priority, self._head)
        elif self._tail.priority > priority:
            self._tail.next = PQNode(item, priority)
        else:
            temp = self._head
            while temp.next is not None and temp.next.priority > priority:
                temp = temp.next
            temp.next = PQNode(item, priority, temp.next)
        self._size += 1
        return self

    def min(self):
        """
            Get the minimum value from queue.
        """
        return self.back()
    
    def max(self):
        """
            Get the maximum value from queue.
        """
        return self.front()