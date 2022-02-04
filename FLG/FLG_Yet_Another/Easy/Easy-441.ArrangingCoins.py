"""
441. Arranging Coins (Easy)

Main Idea:
Binary Search
Сумма арифметической прогресси для N  первых членов при а1 = 1 и d=1  => Sn = (N**2 + N)/2
поэтому делим N пополам, сравниваем с Sn и продолжаем
алгоритм либо слева, либо справа.

При этом mid не отбрасываем

Остановить итерацию, когда lo и hi отличаются на 1

Time complexity: O(logN)

Space complexity: O(N)
Runtime: 40 ms, faster than 79.76% of Python3 online submissions for Arranging Coins.
Memory Usage: 14 MB, less than 87.98% of Python3 online submissions for Arranging Coins.

"""
class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if hi - lo == 1: return mid   # Base Case for 5 =>  between 2 an 3
            sn = (mid ** 2 + mid) / 2

            if sn > n:
                hi = mid
            elif sn < n:
                lo = mid
            else:
                return mid


def test_solution():
    inp = [5,8,2**31-2]
    out = [2,3,65535]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.guessNumber(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()