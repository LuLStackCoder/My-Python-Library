class AbstractLinkedList(object):
    """
        Abstract class representing the LinkedList inteface.
    """
    def __init__(self) -> None:
        """
            Initialize class with head, tail and size of the container.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def size(self) -> int:
        """
            Size of container
        """
        return self._size

    def empty(self) -> bool:
        """
            Сhecking whether the container has at least one element.
        """
        return self._size == 0

    def indexof(self, item) -> int:
        """
            Index of item, -1 if the value isn't in container.
        """
        count = 0
        for i in self:
            if i.item == item:
                return count
            count += 1
        return -1



    def __str__(self) -> str:
        if self._head == None:
            return '[]'
        else:
            string = ''
            for i in self:
                string += f'{i.item}'
                if i.next != None:
                    string += ', '
            return f'[{string}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> object:
        self._iter = self._head
        return self

    def __next__(self) -> object:
        if self._iter != None:
            item = self._iter
            self._iter = self._iter.next
            return item
        else:
            raise StopIteration

    def __getitem__(self, index):
        count = 0
        if index >= self._size:
                raise IndexError('List index out of range')
        for i in self:
            if count == index:
                return i.item
            count += 1
    
    def __setitem__(self, index, value) -> None:
        count = 0
        if index >= self._size:
            raise IndexError('List index out of range')
        for i in self:
            if count == index:
                i.item = value
            count += 1

    def __eq__(self, other) -> bool:
        if self.__class__ == other.__class__:
            if self._size != other._size:
                return False
            for i, j in zip(self, other):
                if i.item != j.item:
                    return False
            return True
        return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __contains__(self, item) -> bool:
        for i in self:
            if i.item == item:
                return True
        return False
