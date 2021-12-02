from queue import *
import pytest

def test_queue_happy():
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(5)
    assert q.items == [5, 8, 3, 1], "Enqueue failure"
    assert q.dequeue() == 1, "Dequeue failure"
    assert q.size() == 3, "Size wrong"

def test_queue_edge():
    q = Queue()
    assert q.dequeue() is None, "Errors not managed properly when dequeuing from empty queue"
    assert q.size() == 0, "Size wrong for empty queue"


