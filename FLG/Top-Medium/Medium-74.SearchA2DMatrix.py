"""
74. Search a 2D Matrix  (Medium)

Main Idea.
1)  сделать из матрицы лист,
по условию получится отсортированный лист
2) Искать target в листе бинарным поиском

Time complexity: O(n) + O(log(n*m))
1) сделать лист  O(n), где n число строк в матрице
2) бинарный поиск O(log(n*m))


Space complexity: extra space O (N*M) for list

Runtime: 64 ms, faster than 30.56% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.8 MB, less than 64.10% of Python3 online submissions for Search a 2D Matrix.
"""
class Solution:
    def searchMatrix(self, matrix, tar):

        def _bin_search(arr, tar):
            if len(arr) == 0: return False                 # Edge case   ([], 3)
            if tar < arr[0] or tar > arr[-1]: return False # Edge case  ([2,3], 0)

            lo = 0
            hi = len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == tar:
                    return True

                if tar < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False

        aux = []            # Make a list from the matrix
        for row in matrix:
            aux.extend(row)

        return _bin_search(aux, tar)


def test_solution():
    inp = [ ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
            ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61),
            ([[2, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0),
            ([[2, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 8),
            ([[1],[3]], 1),
            ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11),
            ([[1, 3]], 3),
            ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30)
          ]
    out = [True, False, False, False, False, True, True, True, True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.searchMatrix(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
