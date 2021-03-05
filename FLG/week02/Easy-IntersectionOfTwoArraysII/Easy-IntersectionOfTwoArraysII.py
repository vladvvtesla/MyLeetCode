"""
350. Easy - Intersection of Two Arrays II

Success, but too slow
Runtime: 96 ms, faster than 6.24% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.5 MB, less than 10.29% of Python3 online submissions for Intersection of Two Arrays II.
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


    def intersect(self, nums1, nums2):
        self.quicksort(nums1, 0, len(nums1)-1)
        self.quicksort(nums2, 0, len(nums2)-1)

        # Choose the biggest array
        if len(nums1) >= len(nums2):
            n1,n2 = len(nums1),len(nums2)
            arr1,arr2 = nums1,nums2
        else:
            n1,n2 = len(nums2),len(nums1)
            arr1,arr2 = nums2,nums1

        res = []
        cur_i = cur_j = 0
        for i in range(cur_i, n1):
            for j in range(cur_j, n2):
                if cur_i == n1:                 # for case i+1 = len(arr1) and error arr1[n1]
                    break
                if arr1[cur_i] == arr2[cur_j]:
                    res.append(arr1[cur_i])
                    cur_i += 1
                    cur_j += 1
                    break
                elif arr1[cur_i] > arr2[cur_j]:
                    cur_j += 1
                else:
                    cur_i += 1

        return res


def test_intersect():
    inp = [[[1,2,2,1],[2,2]],
           [[4,9,5], [9,4,9,8,4]],
           [[4, 7, 9, 7, 6, 7], [5, 0, 0, 6, 1, 6, 2, 2, 4]],
           [[54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41],
            [17, 17, 87, 98, 18, 53, 2, 69, 74, 73, 20, 85, 59, 89, 84, 91, 84, 34, 44, 48, 20, 42, 68, 84, 8, 54, 66, 62, 69, 52, 67, 27, 87, 49, 92, 14, 92, 53, 22, 90, 60, 14, 8, 71, 0, 61, 94, 1, 22, 84, 10, 55, 55, 60, 98, 76, 27, 35, 84, 28, 4, 2, 9, 44, 86, 12, 17, 89, 35, 68, 17, 41, 21, 65, 59, 86, 42, 53, 0, 33, 80, 20]
            ]
           ]
    out = [[2,2], [4,9], [4,6],
           [0, 4, 9, 12, 18, 21, 27, 28, 33, 35, 41, 48, 54, 55, 55, 59, 60, 60, 61, 62, 65, 67, 73, 76, 84, 84, 86, 89, 89, 94]
           ]
    sol = Solution()
    for k in range(len(inp)):
        test_res = sol.intersect(inp[k][0], inp[k][1])
        print("Test", k + 1, ":", "OK" if test_res == out[k] else "Failed")
        print()

if __name__ == '__main__':
    test_intersect()
