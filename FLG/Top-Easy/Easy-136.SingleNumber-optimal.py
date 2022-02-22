"""
136. Single Number (Top-Easy)

Main Idea.
XOR Operation
0 ^ 2 = 2
2 ^ 2 = 0
0 ^ 1 = 1
Return 1

Time complexity: O(N)
Traverse List : O(n)

Space complexity: O(1)

Runtime: 140 ms, faster than 80.23% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 40.32% of Python3 online submissions for Single Number.

"""
class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for val in nums:
            res ^= val
        return res


def test_solution():
    inp = [ [2,2,1],
            [4,1,2,1,2],
            [1]]
    out = [ 1,4,1]
    # inp = [[2,2,1]]
    # out = [1]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.singleNumber(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
