"""
912. Sort an Array

Solution
1) sort array using quicksort in ascending order

Time Complexity:  O( N * lg N )
                  sorting array       O( N * lg N )
Space Complexity: O(N) in-place

Success, but too slow
Runtime: 360 ms, faster than 39.45% of Python3 online submissions for Sort an Array.
Memory Usage: 20 MB, less than 88.56% of Python3 online submissions for Sort an Array.
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

    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums)-1)
        return nums                           # Leetcode needs it


def test_sortArray():
    a = [5,2,3,1]
    a_sorted = [1,2,3,5]
    sol = Solution()
    sol.sortArray(a)
    print("Test", "1.", "OK" if a == a_sorted else "Failed")
    print()

    b = [5,1,1,2,0,0]
    b_sorted = [0,0,1,1,2,5]
    sol = Solution()
    sol.sortArray(b)
    print("Test", "2.", "OK" if b == b_sorted else "Failed")
    print()

if __name__ == '__main__':
    test_sortArray()