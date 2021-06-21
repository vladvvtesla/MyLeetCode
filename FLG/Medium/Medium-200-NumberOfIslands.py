"""

200. Medium - Number of Islands


1. Проверить все элементы матрицы MxN
   Если встретили 1, то увеличиваем num_island нв 1 и  запускаем DFS
2. DFS  перезаписывет посещенную ячейку с 1 на 0, для того чтобы не посещать во второй раз и не суммировать
3. Проверяет ячейки справа, слева, и снизу, сверху
   Если там тоже 1, то рекурсивно запускает DFS

Time complexity: O(NxM)

Runtime: 140 ms, faster than 70.91% of Python3 online submissions for Number of Islands.
Memory Usage: 15.4 MB, less than 51.48% of Python3 online submissions for Number of Islands.
"""


class Solution:
    def dfs(self, grid, r, c):
        """
        r: index of row
        c: index of column
        """
        grid[r][c] = 0  # replace 1 to 0, to not visit this again
        lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]  # list of bottom, up, left, right
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == "1":
                self.dfs(grid, row, col)

    def numIslands(self, grid):
        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
        return num_islands


def test_numIslands():
    inp = [ [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]],
            [[0, 0, 0, 0, 0, 0, 0, 0]],
            [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"] ]
          ]
    out = [1, 0, 3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.numIslands(inp[i])
        print()
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")



if __name__ == '__main__':
    test_numIslands()
