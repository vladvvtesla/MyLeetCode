class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        # Time complexity O(1)
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def size(self):
        count = 0
        cur = self.tail
        while cur:
            count += 1
            cur = cur.next
        return count

    def iter(self):
        cur = self.head
        while cur:
            val = cur.data
            cur = cur.next
            yield val

    def delete(self, data):
        """ Delete node by data it contains.
            It should take a O(n) to delete a node."""
        cur = self.tail
        prev = self.tail
        while cur:
            if cur.data == data:
                if cur == self.tail:
                    self.tail = cur.next
                else:
                    prev.next = cur.next
                self.size -= 1
                return
            prev = cur
            cur = cur.next

    def search(self, data):
        """ Check whether a list contains an item"""
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        """ Clear the entire list. """
        self.tail = None
        self.head = None



if __name__ == '__main__':
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')

    # List traversal
    # current = words.tail
    for word in words.iter():
        print(word)

    # Size
    print('size:', words.size)

    # Search by data
    print('There is "egg" in the List:', words.search('egg'))