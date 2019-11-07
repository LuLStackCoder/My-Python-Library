class Node(object):
    """
        Node class representing each of the linked nodes in the list.
    """
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'{self.item}'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.item == other.item

    def __repr__(self):
        return f'{super().__repr__()}\nValue: {self.item}'

class DoubleNode(object):
    """
        Node class representing each of the doubly-linked nodes in the list.
    """
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'{self.item}'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.item == other.item

    def __repr__(self):
        return f'{super().__repr__()}\nValue: {self.item}'
