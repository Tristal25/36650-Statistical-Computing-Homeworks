class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        try:
            return self.items.pop()
        except IndexError as err:
            print(str(err))
            return None

    def size(self):
        return len(self.items)