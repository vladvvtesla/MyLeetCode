class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        """Time complecity O(1)"""
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        """Time complexity O(1)"""
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1