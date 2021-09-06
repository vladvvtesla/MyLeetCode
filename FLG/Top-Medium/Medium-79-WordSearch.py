"""
79. Word Search - Top Medium

Main Idea:
https://www.youtube.com/watch?v=RqffW0smIbQ  - DFS

Time complexity:

Space complexity:

Runtime: 5268 ms, faster than 81.06% of Python3 online submissions for Word Search.
Memory Usage: 14.2 MB, less than 89.32% of Python3 online submissions for Word Search.
"""


class Solution:
    def exist(self, board, word):
        n = len(board[0])
        m = len(board)
        p = len(word)

        def helper(r, c, pos):
            if pos >= p:
                return True
            elif 0 <= r < m and 0 <= c < n and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                if helper(r - 1, c, pos + 1) or \
                    helper(r + 1, c, pos + 1) or \
                    helper(r, c - 1, pos + 1) or \
                    helper(r, c + 1,pos + 1):
                    return True
                board[r][c] = temp
            return False

        for r in range(m):
            for c in range(n):
                if helper(r, c, 0):
                    return True
        return False




def test_solution():
    # inp = [([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")]
    inp = [([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "e", "E"]], "SEe"),
             ]
    out = [True, True, False, True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.exist(inp[i][0], inp[i][1])
        print()
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")


if __name__ == '__main__':
    test_solution()