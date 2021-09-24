"""
232. Easy - Implement Queue using Stacks

Runtime: 28 ms, faster than 83.81% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 14.3 MB, less than 71.56% of Python3 online submissions for Implement Queue using Stacks.
"""

class MyQueue:

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def push(self, x):
        self.inbound_stack.append(x)

    def pop(self):
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

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())