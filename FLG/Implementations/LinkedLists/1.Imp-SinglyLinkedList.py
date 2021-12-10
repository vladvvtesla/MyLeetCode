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
            self.head.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def size(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        """ Delete node by data it contains.
            It should take a O(n) to delete a node."""
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

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
    current = words.tail
    for word in words.iter():
        print(word)

    # Size
    print('size:', words.size)