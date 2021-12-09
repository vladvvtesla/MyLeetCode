"""
344. Reverse String (Top-easy)


Time Complexity: O(n)

Space Complexity: O(n)

Runtime: 327 ms, faster than 9.75% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 94.72% of Python3 online submissions for Reverse String.
"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for k in range(len(s) // 2 ):
            s[k],s[-1-k] = s[-1-k],s[k]

        return s

def test_solution():
    inp = [["h","e","l","l","o"],
           ["H","a","n","n","a","h"]]
    out = [["o","l","l","e","h"],
           ["h","a","n","n","a","H"]]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.reverseString(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()