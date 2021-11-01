"""
Easy - 1295. Find Numbers with Even Number of Digits

Time complexity: O(N+M)  N - len(nums), M - len(str(num))

Space complexity:

Runtime: 52 ms, faster than 84.12% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 14.2 MB, less than 72.15% of Python3 online submissions for Find Numbers with Even Number of Digits.
"""


class Solution:
    def findNumbers(self, nums):
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1
        return res

def test_Solution():
    inp = [[12,345,2,6,7896], [555,901,482,1771], [], [1]]
    out = [2, 1, 0, 0]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.findNumbers(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_Solution()



