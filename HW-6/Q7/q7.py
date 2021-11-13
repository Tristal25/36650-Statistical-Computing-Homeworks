class Node:
    def __init__(self, data=None):
        self.too_big = None
        self.big = None
        self.small = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif data - self.data >= 10:
                if self.too_big is None:
                    self.too_big = Node(data)
                else:
                    self.too_big.insert(data)
            elif data >= self.data:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
        else:
            self.data = data

    # Print the tree
    def traversal(self):
        if self.small:
            self.small.traversal()
        print(self.data)
        if self.big:
            self.big.traversal()
        if self.too_big:
            self.too_big.traversal()

    def traversal_list(self, items):
        if self.small:
            self.small.traversal_list(items)
        items.append(self.data)
        if self.big:
            self.big.traversal_list(items)
        if self.too_big:
            self.too_big.traversal_list(items)
        return items

    def delete(self, data):
        items = []
        items = self.traversal_list(items)
        if data not in items: return
        items.remove(data)
        self.data, self.too_big, self.small, self.big = None, None, None, None
        for item in items:
            self.insert(item)



root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)


print("Tree contents after insertion using the traversal():")
root.traversal()

root.delete(45)

print("Tree contents after deleting 45 using the traversal():")
root.traversal()