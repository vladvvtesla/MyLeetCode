"""
1828. Queries on Number of Points Inside a Circle (Medium)

Main Idea.
Брутфорс
0) по уравнению окружности c центром в (xc,yc), (x-xc)^2 + (y-yc)^2 = r^2

1) проверить все точки в points, находятся ли они внутри окружности,
подставить в уравнение и проверить, что получившееся число по модулю <= R

2) количество найденных точек сложить и добавить в ррезультат

3) повторить для всех окружностей

Сложность O(N*M) N - points, M - circles

Для Брутфорс
Runtime: 3194 ms, faster than 33.66% of Python3 online submissions for Queries on Number of Points Inside a Circle.
Memory Usage: 14.2 MB, less than 87.33% of Python3 online submissions for Queries on Number of Points Inside a Circle.

Оптимизация 1.
Есть точки которые точно не попадают в круг,
для таких точек можем не решать уравнение окружности,
а можем сразу их отбрасывать
Тогда сложность немного уменьшится

Time complexity: O(N*M)

Space complexity: O(1)
"""


class Solution:
    def countPoints(self, points, queries):
        res = [0]*len(queries)
        for p in points:
            for k,c in enumerate(queries):
                if (max(p) <= c[0] + c[2] or max(p) >= c[0] - c[2]):
                    if  (p[0]-c[0])**2 + (p[1]-c[1])**2 <= c[2]**2:
                        res[k] += 1
        return res


def test_solution():
    inp = [ [[[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]],
            [[[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]]
            ]
    out = [[3,2,2],
           [2,3,2,4],
           ]
    # inp = [[[[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]]]
    # out = [[3,2,2]]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.countPoints(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")




if __name__ == '__main__':
    test_solution()
