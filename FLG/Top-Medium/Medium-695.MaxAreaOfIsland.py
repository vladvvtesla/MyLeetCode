"""

695. Medium - Max Area of Island

Долго возился и подсмотрел.
https://www.youtube.com/watch?v=jbeRlfKxo60

1. Проверить все элементы матрицы MxN
   Если встретили 1, то запускаем DFS
2. DFS  перезаписывет посещенную ячейку с 1 на 0, для того чтобы не посещать во второй раз
3. Проверяет ячейки с права и снизу
   Если там тоже 1, то рекурсивно запускает DFS

Time complexity: O(NxM)

Runtime: 140 ms, faster than 76.96% of Python3 online submissions for Max Area of Island.
Memory Usage: 17.2 MB, less than 28.79% of Python3 online submissions for Max Area of Island.
"""


class Solution:
    def dfs(self, grid, r, c):
        """
        r: index of row
        c: index of column
        """
        grid[r][c] = 0  # replace 1 to 0, to not visit this again
        num = 1         # initialize number of 1s
        lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]  # list of bottom, up, left, right
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num

    def maxAreaOfIsland(self, grid):
        area_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, self.dfs(grid, r, c))
        return area_islands


def test_maxAreaOfIsland():
    inp = [ [[0,1], [0,1]],
            [[0, 0, 0, 0, 0, 0, 0, 0]],
            [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
            ]
    out = [2, 0, 6]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.maxAreaOfIsland(inp[i])
        print()
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")



if __name__ == '__main__':
    test_maxAreaOfIsland()
