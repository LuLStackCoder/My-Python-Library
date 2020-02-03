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

class DoubleNode(Node):
    """
        Node class representing each of the doubly-linked nodes in the list.
    """
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

class PQNode(Node):
    """
        Node class representing each of the linked nodes with priority in the pqueue.
    """
    def __init__(self, item, priority, next=None):
        self.item = item
        self.priority = priority
        self.next = next

class BSTreeNode(Node):
    """
        Node class representing each of the binary tree nodes.
    """
    def __init__(self, key, item, left=None, right=None, parent=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.right:
                    yield elem

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self,key,item,left,right):
        self.key = key
        self.payload = item
        self.left = left
        self.right = right
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self
