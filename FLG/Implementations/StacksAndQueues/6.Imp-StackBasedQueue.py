class Queue:
    def __init__(self):
        self.first = []     # inbound stack
        self.second = []    # outbound_stack

    def enqueue(self, data):
        self.first.append(data)

    def dequeue(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second.pop()

    def peek(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second[len(self.second)-1]

    def empty(self):
        if self.second or self.first:
            return False
        else:
            return True


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.first)
    queue.dequeue()
    print(queue.first)
    print(queue.second)
    queue.dequeue()
    print(queue.second)
    print(queue.peek())
    print(queue.empty())