"""
Top-Medium 73. Set Matrix Zeroes

Main Idea:

Решение в лоб
1) Пробежать по матрице, найти все 0 и записать индекс столбца и строки
2) пробежать второй раз и,
   если индекс строки или столбца записан, то переписать значение на 0


Time complexity: O()

Space complexity: O()

Runtime: 160 ms, faster than 39.84% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 15.1 MB, less than 74.22% of Python3 online submissions for Set Matrix Zeroes.
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        zrows = []
        zcols = []
        for ridx, row in enumerate(matrix):
            for cidx, val in enumerate(row):
                if val == 0:
                    zrows.append(ridx)
                    zcols.append(cidx)

        for ridx, row in enumerate(matrix):
            for cidx, val in enumerate(row):
                if ridx in zrows or cidx in zcols:
                    matrix[ridx][cidx] = 0


def test_solution():
    inp = [
          [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
          [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
          ]
    out = [
          [[1,0,1],[0,0,0],[1,0,1]],
          [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
          ]
    for i in range(len(inp)):
        sol = Solution()
        sol.setZeroes(inp[i])
        print('test_res', inp[i])
        print("Test", i + 1, ":", "OK\n" if inp[i] == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()