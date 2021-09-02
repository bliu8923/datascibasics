class Node:

    def __init__(self, val, nval=None):
        val = val
        nxt = nval

    def setNext(self, nval):
        self.nxt = nval


class DLNode(Node):

    def __init__(self, val, nval=None, pval=None):
        super().__init__(val, nval)
        prv = pval

    def setNext(self, nval):
        super().setNext(nval)

    def setPrev(self, pval):
        self.prv = pval


class LinkedList:

    def __init__(self):
        start = None
        curr = None
        length = 0

    def __len__(self):
        return self.length

    def append(self, val):
        nVal = Node(val)
        self.curr.setNext(nVal)
        self.curr = nVal
