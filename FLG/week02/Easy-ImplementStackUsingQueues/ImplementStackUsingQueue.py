class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkedQueueOfStrings():
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first == None

    def enqueue(self, item):
        current = self.first
        if self.first:
            while current.next:
                current = current.next
            current.next = item
        else:
            self.first = Node()
            self.first.item = item
            self.first.next = None

#    def enqueue(self, item):
#        """ Push element x onto end of queue """
#        oldlast = self.last
#        self.last = Node()
#        self.last.item = item
#        self.last.next = None
#        if self.isEmpty:                   # special case for empty queue
#            self.first = self.last
#        else:
#            oldlast.next = self.last
#        print(self.first.item)
#        print(self.last.item)

    def dequeue(self):
        """ """
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty:                       # special case for empty queue
            self.first = None
        return item


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = LinkedQueueOfStrings()
        self.q2 = LinkedQueueOfStrings()
        self.tmp = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        For ImplementStackUsingQueues: we should find full queue, and enqueue new item into it
        """
        self.q2.enqueue(x) if self.q1.isEmpty() else self.q1.enqueue(x)

        print('==== push ====')
        print('q1 empty', self.q1.isEmpty())
        print('q2 empty', self.q2.isEmpty())
        print('')

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        For ImplementStackUsingQueues:
        1) Replace N-1 item from full queue to empty queue
        2) Check if it is the last item and return it
        """
        if self.q1.isEmpty():          # Find an empty queue. It will be fulled by items
            firstq, secondq = self.q2, self.q1
        else:
            firstq, secondq = self.q1, self.q2

        self.tmp = None
        while not firstq.isEmpty():
            self.tmp = firstq.dequeue()
            if firstq.isEmpty(): # the first queue is empty => tmp is last item
                print('==== pop ====')
                print('q1 empty', self.q1.isEmpty())
                print('q2 empty', self.q2.isEmpty())
                return self.tmp
            else:
                print('==== pop1 ====')
                print('q1 empty', self.q1.isEmpty())
                print('q2 empty', self.q2.isEmpty())
                secondq.enqueue(self.tmp)   # if tmp is last item, add it to the second queue

    def top(self) -> int:
        """
        Get the top element.
        For ImplementStackUsingQueues:
        Removes the element on top of the stack and returns that element.
        For ImplementStackUsingQueues:
        1) Replace N-1 item from full queue to empty queue
        2) Save each item to the temp variable
        3) Check if item is the last item
        4) Enqueue the last item, and return the temp
        """
        if self.q1.isEmpty():                    # Find an empty queue. It will be fulled by items
            firstq, secondq = self.q2, self.q1
        else:
            firstq, secondq = self.q1, self.q2

        self.tmp = None
        while not firstq.isEmpty():
            self.tmp = firstq.dequeue()
            secondq.enqueue(self.tmp)       # add item to the second queue

        print('==== top ====')
        print('q1 empty', self.q1.isEmpty())
        print('q2 empty', self.q2.isEmpty())
        return self.tmp


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        For ImplementStackUsingQueues:  Both queue should be empty
        """
        print('==== empty ====')
        print('q1 empty', self.q1.isEmpty())
        print('q2 empty', self.q2.isEmpty())
        return self.q1.isEmpty() and self.q2.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)

    print(obj.pop())
    print(obj.pop())
    print(obj.pop())

    param_2 = obj.top()    # Should return 2
    print('param_2 ', param_2)
    print()
    param_3 = obj.pop()    # Should return 2
    print('param_3 ', param_3)
    print()
    param_4 = obj.empty()  # Should return False



    print('param_4 ', param_4)



