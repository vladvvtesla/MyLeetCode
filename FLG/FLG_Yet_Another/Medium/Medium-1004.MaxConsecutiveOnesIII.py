"""
1004. Max Consecutive Ones III (Medium)

Main Idea.
Sliding Window

1) В начале lo и hi = 0
1) пройтись по всему nums, двигая hi вправо
   2) если встретили 0, то заменить на 1.
      При этом k -= 1, то есть осталось на 1 меньше возможностей заменить 0 на 1
   3) если встретили 1, двигаемся дальше
   4) если k < 0, то есть больше нельзя заменить 0 на 1
      то двигаем вперед lo.
      5) k при этом увеличиваем или нет, в зависимости на что указывает lo

Вернуть hi-lo + 1, так как lo и hi будут указывать на начало и конец максимального диапазона

Time complexity: O(N)

Space complexity: O(1)

Runtime: 666 ms, faster than 68.56% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.6 MB, less than 82.56% of Python3 online submissions for Max Consecutive Ones III.
"""
class Solution:
    def longestOnes(self, nums, k):
        lo = 0                         # lo - left index
        for hi, v in enumerate(nums):  # hi - right index
            k -= (1 - v)
            if k < 0:
                k += 1 - nums[lo]
                lo += 1
        return hi - lo + 1


def test_solution():
    inp = [ ([1,1,1,0,0,0,1,1,1,1,0], 2),
            ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3),
            ([1], 1),
            ([0], 1)
          ]
    out = [6, 10, 1 ,1]
    # inp = [([1,1,1,0,0,0,1,1,1,1,0], 2)]
    # out = [6]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.longestOnes(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
