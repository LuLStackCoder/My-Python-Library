import pytest
from structures import LinkedList
from structures import Stack
from structures import Queue
from structures import Deque
from structures import DoublyLinkedList
from structures import PriorityQueue
from structures import BinarySearchTree

def test_linked_list():
    l = LinkedList([1, 2, 3])
    assert l._head.item == 1
    assert l._tail.item == 3
    assert l.size() == 3
    assert l.empty() is False
    assert l[0] == 1
    assert l[1] == 2
    assert l[2] == 3

    m = LinkedList()
    assert m._head == None
    assert m._tail == None
    assert m.size() == 0
    assert m.empty() is True
    

    # m.append(1)
    # m[0] == 1
    # assert m.size() == 1
    # assert m.empty() is False
    # assert m != l
    # m.append(2)
    # m.append(3)
    # assert m == l
    # assert m is not l
    m.append(9)
    m.prepend(10)
    print(m)
    m.insert(1, 3)
    m.insert(2, 69)
    print(m)
    m.insert(1, 4)
    m.insert(5, 45)
    m.insert(2, 11)
    m.insert(100, 54)
    m.insert(0, 96)
    print(m)
    print(m)
    # print(m.indexof(11))
    m.pop(3)
    m.remove(96)
    m.reverse()
    print(m)
    m.clear()
    print(m._head, m._tail)
    print(m)
    # print(m._head._value)
    # print(m._tail._value)
    # print(m[0])
    # assert m.__str__() == '[1, 3]'
    # assert m._head._next._value == 3
    # assert m._tail._value == 3
    # print(m)
    l = LinkedList([1])
    print(l)
    l.pop()
    print(l)

# test_linked_list()


def test_stack():
    t = Stack([54, 27])
    print(t.peek())
    t.clear()
    # t.peek()
    t.push(10)
    t.push(15)
    t.push(20)
    print(t)
    t.clear()
    print(t)
    t.push(2)
    print(t)
    print(t.peek())
    # t.pop()
    # print(t.peek())
    # t.pop()
    # print(t)

# test_stack()

def test_queue():
    q = Queue([48, 3])
    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(20)
    q.enqueue(25)
    print(q.indexof(25))
    print(q)
    q.clear()
    # q.pop()
    print(q._head, q._tail)
    print(q)
    q.enqueue(25)
    q.dequeue()
    print(q)

# test_queue()

def test_deque():
    d = Deque([48, 3])
    d.append(49)
    d.append(55).prepend(54).prepend(27).append(30)
    print(d)
    d.shift()
    d.pop()
    d.clear()
    # d.pop()
    print(d._head, d._tail)
    print(d)

# test_deque()

def test_dllist():
    l = DoublyLinkedList([54, 27])
    l.pop()
    l.reverse
    print(l)
    l.append(10).prepend(20).append(40).prepend(30)
    print(l)
    l.reverse()
    print(l)
    l.pop_at(4)
    l.shift()
    l.insert(0, 69)
    l.insert(0, 69)
    l.insert(15, 70)
    l.insert(4, 71)
    l.insert(6, 72)
    # l.remove(27)
    l.remove(71)
    l.remove(72)
    l.remove(69)
    l.remove(69)
    print(l)
    l.pop()
    l.clear()
    # l.pop()
    l.reverse()
    print(l)

# test_dllist()

def test_pqueue():
    q = PriorityQueue([1, 2, 3, 4])
    print(q)
    q.clear()
    q.enqueue(1, 4).enqueue(3, 5).enqueue(4, 6).enqueue(1, 9).enqueue(5, 10)
    print(q)
    print(q.max())
    print(q.min())

# test_pqueue()

b = BinarySearchTree()
b.insert(10, 'yellow')
b.insert(22, 'green')
b.insert(5, 'red')
b.insert(1, 'blue')
b.insert(21, 'purple')
# print(b._root)
b.bfs(b._root)
# b[10] = 'pink'
# print(b[10])