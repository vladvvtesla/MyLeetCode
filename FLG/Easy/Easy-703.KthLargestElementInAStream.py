"""

703. Kth Largest Element in a Stream (Easy)

Main Idea:
Чтобы использовать MinHeap в каччестве MaxHeap достаточно изменить знаки всех элементов в nums
Создать MaxHeap размером k
По очереди добавить в него все элементы из nums, наименьшие будут вытесняться
на вершине MinHeap будет максимальный элемент из К самых больших,
а на дне MinHeap юудет К-й из самых больших
То есть его и возвращаем.


Time complexity: O(n)
Изменить знаки всех элементов в nums: O(n)
Добавить nums в MinHeap - heap.heapify(nums): O(n)
Вернуть k-й элемент от вершины O(1), так как это просто обращение к k-му элементу в списке

Space Complexity: extra space for heap

Runtime: 1121 ms, faster than 8.59% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.1 MB, less than 93.53% of Python3 online submissions for Kth Largest Element in a Stream.

"""

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        mimus_nums = [el * (-1) for el in nums]
        mimus_nums.sort()
        self.h = mimus_nums[:self.k]

    def add(self, val):
        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
        self.h.append(val*(-1))
        self.h.sort()
        if len(self.h) > self.k:      #   For edge case:  k = 1, nums = []
            self.h.pop()
            return (self.h[self.k-1]) * (-1)
        else:
            return self.h[-1] * (-1)


def test_solution():
        inp = [[3, [4, 5, 8, 2], [3, 5, 10, 9, 4]],
               [1, [], [-3, -2, -4, 0, 4]],
               [3, [5, -1], [2,1,-1,3,4]]
               ]
        out = [[None, 4, 5, 5, 8, 8],
               [None,-3,-2,-2,0,4],
               [None, -1, 1, 1, 2, 3]
               ]
        for i in range(len(inp)):
            obj = KthLargest(inp[i][0], inp[i][1])
            test_res = [None]
            for el in inp[i][2]:
                test_res.append(obj.add(el))
            print()
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_solution()