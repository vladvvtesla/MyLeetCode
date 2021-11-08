"""
Top-Medium 56.Merge Intervals

Time Complexity: O(N)

Space Complexity: O(N)

Runtime: 84 ms, faster than 82.84% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.1 MB, less than 55.51% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals):
        sl = sorted(intervals)                   # Sorted List of intervals

        for idx in range(len(sl)-1):
            if sl[idx][1] >= sl[idx+1][0]:
                if sl[idx+1][1] >= sl[idx][1]:
                    sl[idx][1] = sl[idx+1][1]    # merge intervals
                sl[idx + 1] = sl[idx][:]         # Replace merged interval by new
                sl[idx] = None                   # Replace old interval by None

        return [el for el in sl if el is not None]  # Delete Nones


def test_solution():
    inp = [[[1,3],[2,6],[8,10],[15,18]],
           [[1, 4], [4, 5]],
           [[1, 4], [5, 6]],
           [[1, 4], [0, 0]],
           [[0,0],[0,0]],
           [[1, 4], [2, 3]],
           [[1, 4], [0, 2], [3, 5]],
           [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
           ]
    out = [[[1,6],[8,10],[15,18]],
           [[1,5]],
           [[1,4],[5,6]],
           [[0, 0], [1, 4]],
           [[0,0]],
           [[1,4]],
           [[0,5]],
           [[1,3],[4,7]]
           ]
    sol = Solution()

    for i in range(len(inp)):
        test_res =  sol.merge(inp[i])
        print('test_res = ', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
