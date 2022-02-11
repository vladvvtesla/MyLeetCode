"""
Easy - 977. Squares of a Sorted Array


Main Idea:
1) squares using list comprehensing
2) Sort using quicksort


Time complexity: O(NlogN)
squares O(N)
Sorting O(NlogN)

Space Complexity: O(N)

Runtime: 204 ms, faster than 95.93% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.1 MB, less than 57.11% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:

    def sortedSquares(self, nums):
        nums = [k*k for k in nums]
        return sorted(nums)


def test_solution():
    inp = [[-4,-1,0,3,10],
           [-7,-3,2,3,11]
          ]
    out = [[0,1,9,16,100],
            [4,9,9,49,121]]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.sortedSquares(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()