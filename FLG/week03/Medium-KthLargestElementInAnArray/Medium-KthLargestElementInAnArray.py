"""
215. Kth Largest Element in an Array

Solution
1) sort array using quicksort in ascending order
2) return -kth item of sorted array

Time Complexity:  O( N * lg N )
                  sorting array       O( N * lg N )
                  return -kth item    O(1)
Space Complexity: O(N)  in-place sorting

Success, but too slow
Runtime: 5060 ms, faster than 5.01% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 19.3 MB, less than 6.18% of Python3 online submissions for Kth Largest Element in an Array.
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


    def findKthLargest(self, nums, k: int) -> int:
        self.quicksort(nums, 0, len(nums)-1)
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