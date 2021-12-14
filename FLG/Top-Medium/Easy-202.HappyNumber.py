"""
202. Easy - Happy Number (Top Medium)



Main Idea:

Time Complexity:

Space Complexity:

Runtime: 36 ms, faster than 63.61% of Python3 online submissions for Happy Number.
Memory Usage: 14.4 MB, less than 16.29% of Python3 online submissions for Happy Number.
"""


class Solution:
    def isHappy(self, n):
        iset = set()

        def _isHappy(n, iset):

            if n in iset:
                return False
            else:
                iset.add(n)

            ilist = []
            while n:
                ilist.append(n % 10)
                n //= 10

            if len(ilist) == 1 and ilist[0] == 1:
                return True
            elif len(ilist) >= 1:
                n = 0
                for idx in range(len(ilist)):
                    n += ilist[idx] ** 2
                return _isHappy(n, iset)

        return  _isHappy(n, iset)


def test_solution():
    inp = [19, 2, 123]
    out = [True, False, False]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.isHappy(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()