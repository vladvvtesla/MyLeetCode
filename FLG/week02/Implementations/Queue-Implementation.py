"""
Segewick - w2 - queue implementation using Singly-Linked-list
"""


class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkedQueueOfStrings():
    def __init__(self, first=None):
        self.first = first
        self.last = None

    def isEmpty(self):
        """ Returns whether the queue is empty. """
        return self.first == None

    def enqueue(self, item):
        """ Push element x onto end of queue """
        oldlast = self.last
        last = Node()
        last.item = item
        last.next = None
        if self.isEmpty:                   # special case for empty queue
            self.first = self.last = last
        else:
            oldlast.next = last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty:                       # special case for empty queue
            self.first = None
        return item