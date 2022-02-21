"""
268. Missing Number (Easy)

Main Idea.
1) Длина входного массива сразу говорит нам, о каком диапазоне идет речь
2) Len(nums) = 3, значит, [0,1,2,3]
3) сумма арифметической прогрессии в данном случае (0+3)*4/2 = 6
4) и теперь остается пробежаться по nums
  и последовательно вычесть все числа. 6-0-3-1 = 2,
  значит в последовательности не хватает числа 2

Time complexity: O(n)

Space complexity: O(1)

Runtime: 239 ms, faster than 31.44% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 72.35% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        s = n * (n + 1) / 2
        for val in nums:
            s -= val
        return int(s)


def test_solution():
    inp = [ [3,0,1],
            [0,1]
          ]
    out = [2,2]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.missingNumber(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
