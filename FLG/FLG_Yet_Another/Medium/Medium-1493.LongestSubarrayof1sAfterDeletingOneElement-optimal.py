"""
1493. Longest Subarray of 1's After Deleting One Element (Medium)

Main Idea.
1) Одина раз пробежаться по nums
2) вначале f и s равны 0
f - указывает на самый левый элемент
s - это дистанция от f
4) Если val == 1
    то дистанция увеличивается, а res равен max(res, f + s)
5) Когда прошли весь nums,
    еще раз проверяем, чтобы res = max(res, f + s)   # для [1,1,0,1]

#                        val
# 0, 1, 1, 1, 0, 1, 1, 0, 1
#   s f
# res = 5

Time complexity: O(n)

Space complexity: O(1)

Runtime: 382 ms, faster than 87.37% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
Memory Usage: 16.7 MB, less than 27.53% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
"""
class Solution:
    def longestSubarray(self, nums) -> int:
        n = len(nums)
        if n == 0: return 0                # Edge case []
        if sum(nums) == n: return n - 1    # Edge case [1,1,1]

        first = second = 0                     #                 k
        res = 0                                # 0,1,1,1,0,1,1,0,1
        for val in nums:                       #   s f
            if val == 0:                       # res = 5
                res = max(res, first + second)
                first = second                 # это вообще не очевидно
                second = 0
            else:
                second += 1
        res = max(res, first + second)
        return res


def test_solution():
    inp = [ [1,1,0,1],
            [0,1,1,1,0,1,1,0,1],
            [1, 1, 1],
            [0, 1, 1, 1],
            [1],
            [1, 0, 0, 0, 0],
            [0, 0, 0]
            ]
    out = [3,5,2,3,0, 1, 0]
    # inp = [[1,1,0,1]]
    # out = [3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.longestSubarray(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
