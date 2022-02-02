"""
69. Sqrt(x) (Easy)

Main Idea.
Binary Search
if mid * mid > x  => choose left half-array

Time complexity: O(logN)

Space complexity: O(N)

Runtime: 65 ms, faster than 35.34% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.7 MB, less than 99.66% of Python3 online submissions for Sqrt(x).

"""
class Solution:
    def mySqrt(self, x):
        if x <= 1 : return x          # Edge cases: 0^2 = 0, 1^2 = 1

        lo = 1
        hi = x
        while lo <= hi:
            if hi - lo <= 1:          #  For x = 9 => [2,3] => return 2
                return lo             #  For x = 3 => [1] => return 1

            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid
            else:
                hi = mid

        return mid


def test_solution():
    inp = [6,3,25,4,8,0,1]
    out = [2,1,5,2,2,0,1]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.mySqrt(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
