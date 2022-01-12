"""
46. Permutations (Top-Medium)


Main Idea: DP
1) Взять subarray [0], решение для него одно: [0] - > Добавить в список q

2) Бежать по этому списку q циклом
3) добавить к первуму subarray следующее число из nums[1] = 1,
    индекс для этого равен длине промежуточного решения
    если промежуточное решение равно [0], то индекс равен 1, поэтому добавляем nums[1] = 1
    Зптем найти все новые перестановки для [0,1]
    полученные перестановки добавить в тот же список q

    Как генерить новые перестановки
    def _permut()
    бежим по подмассиву от последнего элеменнта к первому и меняем поочереди элементы местами
    [0], 1 ->  [0,1], [1,0]
4) добавить к subarray следующее число 2, и
    определить, какие дополнительные ответы получатся
    [0,1]:   [2,0,1], [0,2,1], [0,1,2],
    [1,0]:   [2,1,0], [1,2,0], [1,0,2]
5) Продолжать добавлять в q, пока длина промежуточного решения не сравняется с длиной nums
6) И тогда последние n! элементов q и будут нашим списком всех перестановок


Time complexity: O (n * n!)
O(n), чтобы пройтись по всему списку
Чтобы из n чисел сделать все перестановки по n, нужно n! операций
итого O (n * n!)

Space complexity:
генерится очень много списков с промежуточными перестановками,
это совсем не оптимально


Runtime: 48 ms, faster than 31.37% of Python3 online submissions for Permutations.
Memory Usage: 14.6 MB, less than 14.92% of Python3 online submissions for Permutations.
"""


class Solution:
    def permute(self, nums):
        def _permut(arr, x):
            """Generate new permutations [0], 1  --->  [ [0,1][1,0] ] """
            p = arr[:]
            p.append(x)

            res = [p[:]]
            for k in range(len(p)-1, 0, -1):
                p[k],p[k-1] = p[k-1],p[k]
                res.append(p[:])

            return res

        q = [[]]
        for val in q:
            while len(val) < len(nums):
                for el in _permut(val, nums[len(val)]):
                    q.append(el)
                break

        # после цикла while в очереди останутся все наши перестановки длиной len(nums)
        # поэтому остается вернуть только сам queue ввиде списка
        return [el for el in q if len(el) == len(nums)]


def test_solution():
        inp = [[0,1],
               [1],
               [1,2,3]]
        out = [[[0,1],[1,0]],
               [[1]],
               [[1, 2, 3], [1, 3, 2], [3, 1, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1]]]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.permute(inp[i])
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()


