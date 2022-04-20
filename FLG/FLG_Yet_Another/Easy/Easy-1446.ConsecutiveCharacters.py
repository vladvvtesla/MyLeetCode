"""
1446. Consecutive Characters (Easy)


Main Idea:
Two pointers

Time Complexity:
Пройтись по всему списку: O(n)

Space Complexity:
Constant: O(1)

Runtime: 52 ms, faster than 66.32% of Python3 online submissions for Consecutive Characters.
Memory Usage: 13.9 MB, less than 61.17% of Python3 online submissions for Consecutive Characters.

"""


class Solution:
    def maxPower(self, s):
        if len(s) <= 1: return len(s)     # edge case
        res = 0
        cur_res = 1
        n = len(s)-1
        l = r = 0
        while r < n:
            r += 1
            if s[r] != s[l]:
                l = r
                cur_res = 1
            else:
                cur_res += 1
            if cur_res > res:
                res = cur_res

        return res


def test_solution():
        inp = ["leetcode", "abbcccddddeeeeedcba", "", 'j', 'cc', 'ccc', 'accca']
        out = [2, 5, 0, 1, 2, 3, 3]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.maxPower(inp[i])
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()



