from remove_dups_linked_list import *
import pytest

def test_linked_list_node_happy():
    first_node = Node()
    first_node.set_data(11)
    assert first_node.data == 11, "Wrong in set data for Node"

def test_linked_list_insert_happy():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    assert linked_list.head.next.data == 3, "Error when inserting into non-empty linked list"

def test_linked_list_size_happy():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    linked_list.insert(6)
    assert linked_list.size() == 3, "Error in calculating size"

def test_linked_list_print_happy():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    linked_list.insert(6)
    assert linked_list.print_list() is None, "No need to return anything for print_list"

def test_linked_list_rem_dups_happy():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(3)
    linked_list.insert(11)
    linked_list.remove_dups()
    current = linked_list.head
    elements = []
    while current:
        elements.append(current.data)
        current = current.next
    assert elements == [11, 3, 6], "Duplicates not properly removed"

def test_linked_list_empty_list_edge():
    linked_list = LinkedList()
    assert linked_list.head is None, "Error in creating empty linked list"
    assert linked_list.size() == 0, "Wrong size for empty linked list"
    with pytest.raises(ValueError):
        linked_list.print_list()
    linked_list.insert(1)
    assert linked_list.head.data == 1, "Error occurs when inserting values into the empty list"

def test_linked_list_insert_size_edge():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(None)
    assert linked_list.head.next.data is None, "Cannot insert None into the list"
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    linked_list.insert(6)
    size = linked_list.size()
    linked_list.remove_dups()
    assert linked_list.size() == size, "List changed when running remove duplicates when no duplicates present"

