"""
1502. Can Make Arithmetic Progression From Sequence

Main idea
1. Sort using QuickSort
2. calculate difference a[1] - a[0]
3. Get the sequence of differences between k+1 and k-th item
return False if a[k+1] - a[k] != diff

Time Complexity:  O(NlgN)
    O(NlgN) for QuickSort and
    O(N) for getting differences

Space Complexity: O(N)

Runtime: 60 ms, faster than 14.06% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
Memory Usage: 14.2 MB, less than 88.90% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.

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


    def canMakeArithmeticProgression(self, a) -> bool:
        n = len(a)
        if n <= 1:
            return False
        self.quicksort(a, 0, n-1)

        diff = a[1] - a[0]

        for k in range(1,n-1):
            if a[k+1] - a[k] != diff:
                return False
        return True


def test_canMakeArithmeticProgression():
    inp = [[3,5,1], [1,2,4], [1,100], []]
    out = [True, False, True, False]
    sol = Solution()
    for k,item in enumerate(inp,1):
        test_res = sol.canMakeArithmeticProgression(item)
        print(test_res)
        print("Test", k, ":", "OK" if test_res == out[k-1] else "Failed")
        print()


if __name__ == '__main__':
    test_canMakeArithmeticProgression()