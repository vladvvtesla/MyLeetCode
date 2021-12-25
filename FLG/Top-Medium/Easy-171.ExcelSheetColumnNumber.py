"""
171. Excel Sheet Column Number (Tag Easy but in the Top-medium List)


Main Idea,

Time complexity:

Space complexity:

Runtime: 32 ms, faster than 73.84% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14.2 MB, less than 43.04% of Python3 online submissions for Excel Sheet Column Number.

"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ilist = list(columnTitle)
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        aux = dict()
        count = 1
        for char in alpha:
            aux[char] = count
            count += 1

        res = 0                          #   AB = 26  + 2 =  1 * 26**1 + 2*26**0
        power = len(ilist) - 1
        for x in ilist:
            res += aux[x] * (26 ** power)
            power -= 1

        return res


def test_solution():
    inp = [ 'A', 'B', 'C', 'Z', 'AA', 'AB', 'ZY', ]
    out = [   1,   2,   3,  26,   27,   28,  701, ]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.titleToNumber(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()
