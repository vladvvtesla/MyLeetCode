"""
240. Search a 2D Matrix II

Main Idea.
1) сначала ищем в первой строке двоичным поискам,
 а) если нашли, вернуть True
 b) если не нашли, вернуть индекс того элемента, который больше target
 Таким образом мы ограничили сверху число столбцов в которых нужно искать

2) Из полученной урезанной матрицы, составить список из 1 элементов всех строк
  Затем в полученном списке ищем двоичным поискам
   а) если нашли, вернуть True
   b) если не нашли, вернуть индекс того элемента, который больше target
   Таким образом мы ограничили сверху число строк, в которых нужно искать
3) теперь в урезанной матрице ищем в каждой строке двоичным поиском
4) причем искать начинаем с последней сроки а не с первой
5) Не ищем в первой строке, так как уже искали
6) не ищем в первом столбце так как уже искали


Time complexity:
Поиск в первой строке log N
Создать первый столбец M
Поиск в первом столбце log M
Поиск в маленькой матрице (logN ) * M
Итого (logN ) * M, где N и M меньше матрицы (n*m)


Space complexity: O (N*M)

Runtime: 160 ms, faster than 87.41% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.4 MB, less than 92.85% of Python3 online submissions for Search a 2D Matrix II.
"""
class Solution:
    def searchMatrix(self, matrix, target):
        def _bin_search(arr, n):
            """
            :return: If target has found return (-2, idx) else return (-1, last mid)
            """
            mid = 0
            lo = 0
            hi = len(arr) - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if n == arr[mid]: return (-2, mid)
                if n < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return (-1, mid)

        # Make a list from the first column
        first_col = []
        for row in matrix:
            first_col.append(row[0])

        row_res,row_idx = _bin_search(matrix[0], target)
        col_res, col_idx = _bin_search(first_col, target)

        if row_res == -2:
            return True
        elif col_res == -2:
            return True
        else:
            # Make a binary search in a small matrix
            for r in range(col_idx, 0, -1):
                res, idx = _bin_search(matrix[r][:row_idx+1], target)
                if res == -2:
                    return True
            return False


def test_solution():
    inp = [ ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5),
            ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20),
            ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 21),
            ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 15),
            ([[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17], [18, 21, 23, 26]], 7)
          ]
    out = [True, False, True, True, True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.searchMatrix(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
