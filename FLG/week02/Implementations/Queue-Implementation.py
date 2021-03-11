"""
Segewick - w2 - queue implementation using Singly-Linked-list
"""

class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedListQueue():
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        """ Returns whether the queue is empty. """
        return self.first == None

    def enqueue(self, item):
        """ Push element x onto end of queue """
        oldlast = self.last
        self.last = Node(item)
        if self.isEmpty():                   # special case for empty queue
            self.first = self.last
        else:
            oldlast.next = self.last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():                       # special case for empty queue
            self.last.next = None
        return item

    def printList(self):
        cur = self.first
        while (cur):
            print(cur.val, " -> ", end='')
            cur = cur.next
        print("")