"""
392. Is Subsequence (Easy)

Main Idea:
Two pointer
k moves through substring
j moves through tring
If find all substring return True

Time complexity: O(n + m)

Space complexity: O(1) no extra space

Runtime: 63 ms, faster than 16.03% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.1 MB, less than 86.41% of Python3 online submissions for Is Subsequence.
"""
class Solution:
    def isSubsequence(self, s: str, t: str):
        if len(s) == 0: return True         # Edge Case
        if len(t) == 0: return False        # Edge Case
        t_start = 0
        for k in range(len(s)):  # s - substring
            for j in range(t_start, len(t)):
                if s[k] == t[j]:
                    t_start = j + 1
                    if t_start == len(t) and k < len(s) - 1: # Дошли до конца string,
                        return False                        # но не дошли до конца substring
                    break
                elif s[k] != t[j] and j == len(t) - 1:
                    return False  # Не нашли символ в строке

        return True


def test_solution():
    inp = [('abc', 'ahbgdc'),
           ('axc', 'ahbgdc'),
           ('ahbgdc', 'ahbgdc'),
           ('',''),
           ('s', 'bbb'),
           ('abc', ''),
           ('acb', 'ahbgdc'),
          ]
    out = [True, False, True, True, False, False, False]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.isSubsequence(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()