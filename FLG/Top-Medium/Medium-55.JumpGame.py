"""
55. Jump Game (Top Medium)

Main Idea: Greedy: O(n)

https://www.youtube.com/watch?v=Yan0cv2cLy8

Brut Force: O(n^n)
DP:  O(n^2) + extra space for cash
Greedy: O(n)

Time complexity: O(n)

Space complexity: O(n)

Runtime: 499 ms, faster than 61.96% of Python3 online submissions for Jump Game.
Memory Usage: 15.4 MB, less than 36.71% of Python3 online submissions for Jump Game.

"""


class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


def test_solution():
    inp = [[2,3,1,1,4],
           [3, 2, 1, 0, 4],
           [1],
           [9,1],
           [3, 0, 8, 2, 0, 0, 1],
           [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]
          ]
    out = [True, False, True, True, True, True]
    sol = Solution()

    for i in range(len(inp)):
        test_rest = sol.canJump(inp[i])
        print('test_rest', test_rest)
        print("Test", i + 1, ":", "OK\n" if test_rest == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()