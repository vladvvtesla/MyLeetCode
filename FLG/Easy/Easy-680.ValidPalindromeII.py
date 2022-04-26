"""
680. Valid Palindrome II (Easy)

Main Idea.

Time complexity: O(N)

Space complexity: O(n)

Runtime: 140 ms, faster than 77.68% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.5 MB, less than 51.64% of Python3 online submissions for Valid Palindrome II.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def _validPalindrome(a):
            n = len(a)
            for k in range(n // 2):
                if a[k] != a[n - k - 1]:
                    return False
            return True

        n = len(s)
        for k in range(n // 2):
            if s[k] != s[n - k - 1]:
                s1 = s[k: n - k - 1]
                s2 = s[k + 1: n - k]
                return _validPalindrome(s1) or _validPalindrome(s2)
        return True


def test_solution():

    inp = [ "aba", "abca", "abc", "aac", "abac"]
    out = [ True, True, False, True, True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.validPalindrome(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
