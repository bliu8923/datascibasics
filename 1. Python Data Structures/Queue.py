class Queue:

    def __init__(self):
        items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop([0])

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


