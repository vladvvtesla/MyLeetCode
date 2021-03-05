"""
324. Wiggle Sort II
Without follow up

Main idea:
1) Sort array
2) fill auxilary array with item feom left half of arrand and right half of array

Time complexity: O(N lgN)
                 quicksort: O(N lgN)
                 filling aux array: O(N)
                 copy aux back to a:  O(N)
Space Complexity: O(N) plus extra space for auxilary array

Success, but too slow
Runtime: 2740 ms, faster than 10.73% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 19.4 MB, less than 8.50% of Python3 online submissions for Wiggle Sort II.

"""

class Solution:
    def quicksort(self, a, lo, hi):
        """
        3-way quicksort: Python implementation
        :param a:  Array
        :param lo: low Index
        :param hi: high index
        """
        if hi <= lo:
            return
        lt, gt = lo, hi
        i = lo
        while i <= gt:
            if a[i] < a[lt]:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif a[i] > a[lo]:
                a[gt], a[i] = a[i], a[gt]
                gt -= 1
            else:
                i += 1

        self.quicksort(a, lo, lt - 1)
        self.quicksort(a, gt + 1, hi)


    def wiggleSort(self, a) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        self.quicksort(a, 0, n-1)

        mid = ((n - 1) // 2) + 1        # 3 for 6 , 4 for 7
        aux = [0] * n

        for k in range(n):
        # start to fill aux from middle and from the end of a =>
        # aux[0] = a[mid-1]
        # aux[1] = a[n-1]
            if k % 2 == 0:
                aux[k] = a[mid - k//2 - 1]
            else:
                aux[k] = a[n - (k//2 + 1)]

        for k in range(n):               # copy all items from wig to a
            a[k] = aux[k]


def test_wiggleSort():
    inp = [[1,5,1,1,6,4], [1,3,2,2,3,1], [1,1,1,2,2,2], [5,5,5,4,4,4,4], [4,5,5,6]]
    out = [[1,6,1,5,1,4], [2,3,1,3,1,2], [1,2,1,2,1,2], [4,5,4,5,4,5,4], [5,6,4,5]]
    sol = Solution()
    for i in range(len(inp)):
        sol.wiggleSort(inp[i])
        print('test_res', inp[i])
        print("Test", i + 1, ":", "OK" if inp[i] == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_wiggleSort()