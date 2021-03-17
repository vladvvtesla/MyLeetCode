"""
1046. Last Stone Weight  - Easy - Binary Heap


# Time complexity:  O(NlgN)
       Create Heap: N * ( append() const + _swim() lgN ) => NlgN
       delMax()   : N * ( pop()  const + _sink() lgN ) => NlgN
       plus 1 or 0 heap.inserts after each two delMax()  => ~ 1/4 N lgN
       delMax them again => ~ 1/4 N lgN

# Space Complecity: O(N)
       size of heap => N

Runtime: 28 ms, faster than 87.06% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.5 MB, less than 20.44% of Python3 online submissions for Last Stone Weight.
"""


class Heap():
    def __init__(self):
        self.a = []                # array for Priority Queue
        self.sz = 0                # Heap size or length of array

    def insert(self, x):
        """Insert item into heap"""
        self.a.append(x)           # O(1)
        self.sz += 1
        self._swim(self.sz - 1)    # O(lgN)

    def delMax(self):
        """Return max element and delete in from heap"""
        if not self.sz:
            return None
        max = self.a[0]
        self.a[0],self.a[-1] = self.a[-1],self.a[0]   # put the last item into the root
        self.a.pop(-1)                                # delete last item and resize array
        self.sz -= 1
        self._sink(0)
        return max

    def isEmpty(self):
        return self.sz == 0

    def _swim(self, k):
        """Promotion in a heap"""
        while k != 0 and self.a[k] >= self.a[(k-1)//2]:
            self.a[k], self.a[(k-1)//2] = self.a[(k-1)//2], self.a[k]
            k = (k-1)//2

    def _sink(self, k):
        """Demotion in a heap"""
        while k+1 <= self.sz:
            j = k  # здесь храним номер позиции с которой будем меняться. В начале запоминаем самого себя.
            if 2*k+1 < self.sz and self.a[2*k+1] > self.a[k]:
                j = 2*k + 1
            if 2*k+2 < self.sz and self.a[2*k+2] > self.a[j]:    # проверим, есть ли правsй потомок
                j = 2*k + 2
            if k == j:   # если k не изменился
                break
            else:
                self.a[k],self.a[j] = self.a[j],self.a[k]
                k = j                  # change k for next iteration


class Solution:
    def lastStoneWeight(self, stones) -> int:
        heap = Heap()
        [heap.insert(k) for k in stones]

        while not heap.isEmpty():
            y = heap.delMax()
            if heap.isEmpty():
                return y
            x = heap.delMax()
            if y > x:
                heap.insert(y - x)
        return 0


def test_lastStoneWeight():
    # inp = [[10,5,4,10,3,1,7,8]]
    # out = [0]
    inp = [[2,7,4,1,8,1], [], [1,1], [10,5,4,10,3,1,7,8]]
    out = [1, 0, 0, 0]
    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.lastStoneWeight(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()

if __name__ == '__main__':
    test_lastStoneWeight()
