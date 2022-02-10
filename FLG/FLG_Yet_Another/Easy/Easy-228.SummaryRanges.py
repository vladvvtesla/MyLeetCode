"""
228. Summary Ranges (Easy)

Main Idea:  Three Pointers
1) Указатель start = 0, end = 0   И End бежит вперед

n = len(nums) - 1
While end <= n
Возможны два варианта
   1) nums[end] - nums[end-1] == 1
          continue
   2) nums[end] - nums[end-1] > 1 or end == n
         то нашли новый интервал, поэтому
         добавить в результат предыдущий интерва
         aux.append(str(start) + "->" str(end-1))
         start = end - 1

Time complexity: O(N)
пройти весь array:  O(N)
проверить условие: O(1)

Space complexity: O(n)
вспомогательный массив aux:  O(n)

Runtime: 32 ms, faster than 77.20% of Python3 online submissions for Summary Ranges.
Memory Usage: 13.9 MB, less than 95.38% of Python3 online submissions for Summary Ranges.

"""
class Solution:
    def summaryRanges(self, nums):
        if len(nums)==1: return [str(nums[0])]     # Edge Case
        aux = []
        n = len(nums) - 1
        start = 0
        end = 0
        cur = 1
        while cur <= n:
            if nums[cur] - nums[cur - 1] > 1:
                if start == end:
                    aux.append(str(nums[end]))
                elif start != end:
                    aux.append(str(nums[start]) + "->" + str(nums[end]))
                start = cur
                end = cur
            else:
                end += 1     #  Сдвигаем End и оставляем на месте start

            if cur == n:
                if start == end:
                    aux.append(str(nums[end]))
                elif start != end:
                    aux.append(str(nums[start]) + "->" + str(nums[end]))

            cur += 1
        return aux


def test_solution():
    inp = [ [0,1,2,4,5,7],
            [0, 2, 3, 4, 6, 8, 9],
            [2**31-4, 2**31-3, 2**31-2,2**31-1],
            [-2 ** 31, 2 ** 31 - 1],
            [0, 2, 4, 6],
            [-1]
          ]
    out = [["0->2","4->5","7"],
           ["0", "2->4", "6", "8->9"],
           ['2147483644->2147483647'],
           ['-2147483648', '2147483647'],
           ['0', '2', '4', '6'],
           ['-1']
           ]
    # inp = [[0,1,2,4,5,7]]
    # out = [["0->2","4->5","7"]]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.summaryRanges(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
