"""
1710. Maximum Units on a Truck (Easy)

Main Idea:
1) отсортировать ящики по их вместимости, в начале списка самык вместительные
2) Заполнять грузовить ящиками из отсортированного списка, пока полностью не заполнится

Time Complexity: O(n log n) + O(n*m)
Сортировка O(n log n), n - число типов ящиков
Заполнение O(n) * O(m) , где m - среднее число ящиков одного типа
Итого O(n log n) + O(n*m)

Space Complexity: O(n)

Runtime: 1893 ms, faster than 7.42% of Python3 online submissions for Maximum Units on a Truck.
Memory Usage: 14.9 MB, less than 12.24% of Python3 online submissions for Maximum Units on a Truck.
"""


class Solution:
    def maximumUnits(self, boxTypes, truckSize) -> int:
        # Sort boxes
        sorted_bxs = sorted([[x[1],x[0]] for x in boxTypes], reverse=True)

        # Fill the truck
        res = 0
        for item in sorted_bxs:
            while truckSize and item[1]:
                res += item[0]
                item[1] -= 1
                truckSize -= 1

        return res


def test_Solution():
    inp = [ ( [[1,3],[2,2],[3,1]], 4),
            ( [[5,10],[2,5],[4,7],[3,9]], 10),
            ( [[11, 1], [1, 10], [4, 0], [0, 9]], 12),
            ( [[1, 10], [2, 15]] , 2),
            ( [[1, 10], [2, 15]], 0)
          ]
    out = [8, 91, 21, 30, 0]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.maximumUnits(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_Solution()