class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float(self, k):
        """
        после того, как мы новый элемент поставили в самую нижнюю ноду,
        Нам нужно поднять этот элемент и поставить на место, чтобы соблюсти условие Min Heap
        """
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def minindex(self, k):
        """
        после того, как мы самый нижний элемент сделали root,
        нам нужно этот элемент спустить вниз и поставить на место
        У нас два выбора, спустить его на место правого child, или на место левого.
        Поэтому этот метод minindex и сравнивает правый и левый child,
        """
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1

    def sink(self, k):
        while k * 2 <= self.size:
            mi = self.minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float(self.size)

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

if __name__ == '__main__':
    h = MinHeap()
    for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
        h.insert(i)

    print(h.heap)

    for i in range(10):
        n = h.pop()
        print(n)
        print(h.heap)