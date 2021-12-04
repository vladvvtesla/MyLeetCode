"""
36. Valid Sudoku   (Top-Easy) , хотя метка Medium

Main Idea:  пробежаться по всей матрице
и заполнить вспомогательную структуру данных List of sets. 0-8 - rows, 9-17 - columns, 18-26 subarrays

1. Взяли элемент [0][0],
   его значение 5, то для
   sets[0] = {5}
   sets[0+9]= {5}
   sets[18]= {5}
2. Взяли элемент [0][1],
   его значение 3, то для
   sets[0] = {5,3}
   sets[1+9]= {3}
   sets[18]= {5,3}

Если же во множество set() хотим добавить не уникальный элемент, то судоку не валидна
В таком случае вернуть False

Time Complexity: O(n^2)

Space Complexity: O(n^2) plus extra spaxe for sets

Runtime: 100 ms, faster than 57.31% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14.3 MB, less than 43.60% of Python3 online submissions for Valid Sudoku.
"""
class Solution:
    def isValidSudoku(self, board):

        def _isNotValid(sets, val, r, c):
            if val not in sets[r]:          # check rows
                sets[r].add(val)
            else:
                return True

            if val not in sets[c+9]:        # check columns
                sets[c+9].add(val)
            else:
                return True

            sub_arr = {0}                        # get subbarray
            if r in {0, 1, 2}:
                if c in {0, 1, 2}:
                    sub_arr = sets[18]
                elif c in {3, 4, 5}:
                    sub_arr = sets[19]
                elif c in {6, 7, 8}:
                    sub_arr = sets[20]
            elif r in {3, 4, 5}:
                if c in {0, 1, 2}:
                    sub_arr = sets[21]
                elif c in {3, 4, 5}:
                    sub_arr = sets[22]
                elif c in {6, 7, 8}:
                    sub_arr = sets[23]
            elif r in {6, 7, 8}:
                if c in {0, 1, 2}:
                    sub_arr = sets[24]
                elif c in {3, 4, 5}:
                    sub_arr = sets[25]
                elif c in {6, 7, 8}:
                    sub_arr = sets[26]

            if val not in sub_arr:             # check subbarray
                sub_arr.add(val)
            else:
                return True

            return False

        _sets = [{k} for k in range(100, 127)] #  List of sets. 0-8 - rows, 9-17 - columns, 18-26 subarrays

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif _isNotValid(_sets, board[r][c], r, c):
                    return False
        return True


def test_solution():
    inp = [
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],

        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],

          ]
    out = [True, False]
    sol = Solution()

    for i in range(len(inp)):
        test_rest = sol.isValidSudoku(inp[i])
        print('test_rest', test_rest)
        print("Test", i + 1, ":", "OK\n" if test_rest == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()