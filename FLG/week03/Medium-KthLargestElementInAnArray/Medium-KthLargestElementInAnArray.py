"""
215. Kth Largest Element in an Array

Solution
1) sort array using mergesort in ascending order
2) return -kth item of sorted array

Time Complexity:  O( N * lg N )
                  sorting array       O( N * lg N )
                  return -kth item    O(1)
Space Complexity: O(N) plus extra space proportional to N

Success:
Runtime: 336 ms, faster than 13.24% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.2 MB, less than 44.88% of Python3 online submissions for Kth Largest Element in an Array.

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
        assert self.isSorted(a)         # Precondition: is sorted
        assert self.isSorted(b)         # Precondition: is sorted

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

        assert self.isSorted(c)  # Postcondition: c is sorted

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

    def findKthLargest(self, nums, k: int) -> int:
        self.mergesort(nums)
        return nums[-k]



def test_findKthLargest():
    inp = [([3,2,1,5,6,4], 2), ([3,2,3,1,2,4,5,5,6], 4)]
    out = [5, 4]
    sol = Solution()
    for k,item in enumerate(inp,1):
        test_res = sol.findKthLargest(item[0],item[1])
        print(test_res)
        print("Test", k, ":", "OK" if test_res == out[k-1] else "Failed")
        print()

if __name__ == '__main__':
    test_findKthLargest()