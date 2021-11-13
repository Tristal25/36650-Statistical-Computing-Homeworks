class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.previous = None

    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")


    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.tail
        self.tail = node
        if current:
            self.tail.previous = current

    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail: return
        temp = self.tail
        if self.tail.data == data:
            self.tail = temp.previous
            print("Node deleted is " + str(self.tail.data))
            return
        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return

    def search(self, data):
        if not self.tail:
            return
        temp = self.tail
        if self.tail.data == data:
            return True

        while temp.previous:
            if temp.previous.data == data:
                return True
            temp = temp.previous
        return False


first_node = Node()
first_node.set_data(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The Linked List is (after insertion):")
linked_list.print_list()

linked_list.delete(6)
print("The Linked List is (after deleting 6):")
linked_list.print_list()

print("Does 5 exist in the Linked List?")
print(linked_list.search(5))

print("Does 5 exist in the Linked List?")
print(linked_list.search(17))