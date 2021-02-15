class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedStackOfStrings():
    """" Stack Implementation using Singly-Linked Lists.  Coursera Sedgewick 1 w2 """
    def __init__(self, first=None):
        self.first = first

    def isEmpty(self):
        """ """
        return  self.first == None

    def push(self, item):
        """"""
        oldfirst = self.first         # Save link to the old head into a tmp variable
        self.first = Node()           # new first node
        self.first.item = item        #
        self.first.next = oldfirst    # create link to the

    def pop(self):
        """"""
        item = self.first.item         # Save link to the old head into a tmp variable
        self.first = self.first.next   # new first node
        return item




class Solution:
    def isValid(self, s: str) -> bool:
        pass


