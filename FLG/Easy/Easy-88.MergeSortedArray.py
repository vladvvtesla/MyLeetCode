"""
Easy - 8 Merge sorted array


Main Idea:

nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]

1. создать вспомогательный массив  с , как копия начала nums1
2. затем также, как и в mergesort, соединить два массива c и nums2 в один массив mnums1


Time complexity: O(N log N)

Space Complexity: O(m+n) plus extra space O(m-n)

Runtime: 24 ms, faster than 99.60% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.3 MB, less than 32.22% of Python3 online submissions for Merge Sorted Array.

"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = nums1[0:m]

        if n == 0: return              # Edge Case

        if m == 0:                     # Edge Case
            for i in range(n):
                nums1[i] = nums2[i]
            return

        if c[-1] <= nums2[0]:            # Just copy, if already sorted
            for i in range(n):
                nums1[i+m] = nums2[i]
            return

        i = j = k = 0
        while i < m and j < n:
            if c[i] <= nums2[j]:
                nums1[k] = c[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
                nums1[k] = c[i]
                i += 1
                k += 1
        while j < n:
                nums1[k] = nums2[j]
                j += 1
                k += 1


def test_solution():
    inp = [([1,2,3,0,0,0], 3, [4,5,6], 3),
           ([1,2,3,0,0,0], 3, [2,5,6], 3),
           ([1], 1, [], 0),
           ([0], 0, [1], 1),
           ([2,0], 1, [1], 1),
           ([0,0,0,0,0], 0, [1,2,3,4,5], 5)
            ]
    out = [[1,2,3,4,5,6],[1,2,2,3,5,6], [1],[1], [1,2], [1,2,3,4,5]]

    for i in range(len(inp)):
        sol = Solution()
        sol.merge(inp[i][0],inp[i][1],inp[i][2],inp[i][3])
        print('test_res', inp[i][0])
        print("Test", i + 1, ":", "OK\n" if inp[i][0] == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()