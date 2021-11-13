class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

def selection_sort(ls):
    for i in range(len(ls)):
        min_idx = i
        for j in range(i + 1, len(ls)):
            if ls[min_idx] > ls[j]:
                min_idx = j

        tmp = ls[i]
        ls[i] = ls[min_idx]
        ls[min_idx] = tmp

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head: return
        temp = self.head

        if self.head.data == data:
            self.head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return

    def sortList(self):
        nums = []
        current = self.head
        while current:
            nums.append(current.data)
            current = current.next

        selection_sort(nums)
        current = self.head
        for i in range(len(nums)):
            current.data = nums[i]
            current = current.next


first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
print("The Linked List is:")
linked_list.print_list()

linked_list.sortList()
print("After sorting, the Linked List is:")
linked_list.print_list()
