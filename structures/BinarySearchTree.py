from .Node import BSTreeNode
from .Queue import Queue

class BinarySearchTree(object):
    def __init__(self):
        self._root = None
        self._size = 0

    def length(self):
        return self._size

    def __len__(self):
        return self._size

    def __iter__(self):
        return self._root.__iter__()

    def __setitem__(self,k,v):
        self.insert(k,v)

    def __getitem__(self,key):
        return self.search(key)

    def __contains__(self,key):
        if self._search(key, self._root):
            return True
        else:
            return False

    def preorder(self, node, fn=print):
        if node is None:
            return
        fn(node.item)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self, node, fn=print):
        if node is None:
            return
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
        fn(node.item)

    def bfs(self, node, fn=print):
        if node is None:
            return
        queue = Queue()
        queue.enqueue(node)
        while queue.size() > 0:
            temp = queue.dequeue()
            fn(temp.item)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)

    def inorder(self, node, fn=print):
        if node is None:
            return
        if node.left:
            self.preorder(node.left)
        fn(node.item)
        if node.right:
            self.preorder(node.right)


    def insert(self, key, item):
        if self._root is None:
            self._root = BSTreeNode(key, item)
        else:
            self._insert(key, item, self._root)
        self._size += 1
        return self._root

    def _insert(self, key, item, curr_node):
        if key == curr_node.key:
            curr_node.item = item
        elif key < curr_node.key:
            if curr_node.hasLeftChild():
                self._insert(key, item, self._root.left)
            else:
                curr_node.left = BSTreeNode(key, item, parent=curr_node)
        else:
            if curr_node.hasRightChild():
                self._insert(key, item, self._root.right)
            else:
                curr_node.right = BSTreeNode(key, item, parent=curr_node)
        return self._root

    def __delitem__(self,key):
        self.delete(key)

    def search(self, key):
        if self._root is None:
            return None
        else:
            res = self._search(key, self._root)
            if res is None:
                return None
            else:
                return res.item

    def _search(self, key, curr_node):
        if curr_node is None:
            return None
        elif key == curr_node.key:
            return curr_node
        elif key < curr_node.key:
            return self._search(key, curr_node.left)
        else:
            return self._search(key, curr_node.right)

    def delete(self, key):
        if self._size > 1:
            node_to_remove = self._search(key, self._root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self._size == 1 and key == self._root.key:
            self._root = None
            self._size -= 1
        else:
            raise KeyError('Error, key not in tree')
    # TO DO: complete remove function
    def remove(self, node):
        pass

