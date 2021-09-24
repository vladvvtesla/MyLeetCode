class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

    def peek(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack[len(self.outbound_stack)-1]

    def empty(self):
        if self.outbound_stack or self.inbound_stack:
            return False
        else:
            return True


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.inbound_stack)
    queue.dequeue()
    print(queue.inbound_stack)
    print(queue.outbound_stack)
    queue.dequeue()
    print(queue.outbound_stack)
    print(queue.peek())
    print(queue.empty())