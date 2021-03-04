"""
912. Sort an Array

Solution
1) sort array using mergesort in ascending order

Time Complexity:  O( N * lg N )
                  sorting array       O( N * lg N )
Space Complexity: O(N) plus extra space proportional to N

Success:
Runtime: 532 ms, faster than 7.24% of Python3 online submissions for Sort an Array.
Memory Usage: 20.5 MB, less than 48.29% of Python3 online submissions for Sort an Array.
"""

class Solution:
    def __init__(self):
        pass

    def mergesort(self, a):
        """ Merging Sort implementation"""
        if len(a) <= 1:
            return                  # in-place sorting, so just return None
        middle = len(a) // 2
        l = [a[i] for i in range(0, middle)]       # Left half of the list
        r = [a[i] for i in range(middle, len(a))]  # Right half of the list
        self.mergesort(l)
        self.mergesort(r)
        c = self.merge(l, r)     # merge two array
        for i in range(len(a)):  # новый отсортированный список скопировать в изначальный
             a[i] = c[i]

    def merge(self, a: list, b: list):
        """
        Merging of two sorted arrays
        :param a:   firts sorted array
        :param b:   second sorted array
        :return c:  sorted array after merging
        """
        # assert self.isSorted(a)         # Precondition: is sorted
        # assert self.isSorted(b)         # Precondition: is sorted

        if a[-1] <= b[0]: c = a + b     # Stop if already sorted:

        c = [0] * (len(a) + len(b))
        i = k = n = 0                   # indexes for arrays a, b, c
        while i < len(a) and k < len(b):
            if a[i] <= b[k]:
                c[n] = a[i]
                i += 1
                n += 1
            else:
                c[n] = b[k]
                k += 1
                n += 1
        while i < len(a):  # insert tail of a into c, if it exists
            c[n] = a[i]
            i += 1
            n += 1
        while k < len(b):
            c[n] = b[k]  # insert tail of b into c, if it exists
            k += 1
            n += 1

        # assert self.isSorted(c)  # Postcondition: c is sorted

        return c

    def isSorted(self, a, asc=True):
        """
        Check if an array is sorted
        :param a: array
        :param asc: ascending or descending
        :return: boolean
        """
        s = 2 * int(asc) - 1  # sign:   int(True)=1 => 2*1-1 = 1

        for i in range(len(a) - 1):
            if s * a[i] > s * a[i + 1]:
                return False
        return True

    def sortArray(self, nums):
        self.mergesort(nums)
        return nums                # Leetcode needs it


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