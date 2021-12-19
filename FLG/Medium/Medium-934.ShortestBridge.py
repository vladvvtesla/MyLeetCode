"""
934. Shortest Bridge (Medium)

Main Idea:
1) Бежать по всем ячейки матрицы, пока не найдем 1.
2) Если нашли 1, то вызвать функцию bfs(x,y), которая возвращает координаты всех КРАЙНИХ ячеек первого острова
и при этом отмечает все посещенные ячейки как 0
3) Затем снова бежать по матрице в поисках следующей 1
4) Если нашли 1, то вызвать функцию bfs(x,y), которая возвращает координаты всех КРАЙНИХ ячеек второго острова

5 Получили два облака точек.
6) Рассчитать расстояния между каждой точкой одного облака до каждой точки второго облака
7) Из полученного  множества расстояний, вернуть самое короткое.

Облака точек можно существенно уменьшить, если брать не все точки острова, а только границы.
Если среди соседей есть 0, то это граница,
если соседи только 1, то не добавляем в облако точек.

Time Complexity:

Space Complexity:

Runtime: 944 ms, faster than 7.19% of Python3 online submissions for Shortest Bridge.
Memory Usage: 21.8 MB, less than 5.31% of Python3 online submissions for Shortest Bridge.

"""


class Solution:
    def shortestBridge(self, grid):
        def _bfs(edges, i, j):
            grid[i][j] = 2                        # Кусочек острова, который посетили

            adj_list = []
            if j + 1 <= len(grid[0])-1:          # Right
                adj_list.append((i, j + 1))
            if j - 1 >= 0:                       # Left
                adj_list.append((i, j - 1))
            if i + 1 <= len(grid)-1:             # Down
                adj_list.append((i + 1, j))
            if i - 1 >= 0:                       # Up
                adj_list.append((i - 1, j))

            # Check If there is 0 among naighbours
            neighbours = [grid[x][y] for x,y in adj_list]
            if 0 in neighbours:
                edges.add((i,j))

            for x,y in adj_list:
                if grid[x][y] == 1:
                    edges = _bfs(edges, x, y)

            return edges

        def unique_pairs(n, m):
            for i in range(n):
                for j in range(m):
                    yield i, j

        loop = 1
        first_edge = set()
        second_edge = set()
        for i,j in unique_pairs(len(grid), len(grid[0])):
            if grid[i][j] == 1:
                if loop == 1:
                    first_edge.add((i,j))  # добавить первую 1, даже если она не на границе
                    first_island_edge = _bfs(first_edge, i, j)
                    loop += 1
                else:
                    second_edge.add((i, j))
                    second_edge = _bfs(second_edge, i, j)

        #  Далее найти расстояния от всех точек первого острова ко всем точкам второго острова
        # И вернуть наименьшее
        pairs = []
        for x in first_edge:
            for y in second_edge:
                pairs.append((x,y))

        distanses = [abs(a[0]-b[0]) + abs(a[1]-b[1])-1 for a,b in pairs]

        return min(distanses)





def test_solution():
        inp = [[[0,1],[1,0]],
               [[1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]],
               [[0, 1, 0], [0, 0, 0], [0, 0, 1]],
               [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
               ]
        out = [1,2,2,1]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.shortestBridge(inp[i])
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()


