"""
374. Guess Number Higher or Lower (Easy)

Main Idea:
Binary Search

Time complexity: O(logN)

Space complexity: O(N)

Runtime: 53 ms, faster than 15.41% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 13.9 MB, less than 89.78% of Python3 online submissions for Guess Number Higher or Lower.
"""
class Solution:
    def __init__(self, pick):
        self.pick = pick          # Pick number

    def guess(self, num):
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        lo = 0
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.guess(mid) == -1:     # mid > pick
                hi = mid - 1
            elif self.guess(mid) == 1:    # mid < pick
                lo = mid + 1
            else:
                return mid


def test_solution():
    inp = [(10, 6),
           (1,1),
           (2, 1),
           (10,10),
           (2**31 -1, 2**31-2)
          ]
    out = [6,1,1,10,2**31-2]

    for i in range(len(inp)):
        sol = Solution(inp[i][1])
        test_res = sol.guessNumber(inp[i][0])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()