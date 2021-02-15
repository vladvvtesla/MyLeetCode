"""
Segewick - w2 stack implementation using array

Linked - list implementation
- Every operation takes constant time in the worst case
- Uses extra time and space to deal with the links

Resizig - array implementation
- Every operation takes constant amortized time
- less wasted space
"""



class ResizingArrayStackOfStrings():
    def __init__(self):
        self.s = [None]     # Initialising array with one element
        self.n = 0          # size of array

    def isEmpty(self):
        return self.n == 0

    def push(self, item):
        """Push new item to stack  Resize array if need"""
        if self.n == len(self.s):             # double size of array s when array is full
            self._resize(2 * self.n)
        self.n += 1                           # increase size of array
        self.s[self.n] = item

    def pop(self):
        """Pop item from the stack"""
        pop_item = self.s[self.n]
        self.s[self.n] = None
        self.n -= 1                            # decrease size of array
        if self.n > 0 and self.n == len(self.s) / 4:  # halve size of array s when the arrsy is one-quarter full
            self._resize(len(self.s) / 4)
        return pop_item

    def _resize(self, capacity):
        copy = [None] * capacity
        [copy[i] = self.s[i] for i in range(capacity / 2)]
        self.s = copy