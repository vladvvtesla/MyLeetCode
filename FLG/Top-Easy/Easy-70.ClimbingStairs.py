"""
70. Climbing Stairs (Top-Easy)


Main Idea:
F(4) = F(3) + F(2)
F(2) = F(0) + F(1)
F(0) = 1    - virtual stair place (equals 1  for simplisity)
F(1) = 1
F(2) = 1 + 1 = 2

F(n) = F(n-1) + F(n+2)

1) Make aux list [0, 1, ..., n]
2) Fill all elemenents of aux
aux[n] = aux[n-1] + aux[n-2]

Time Complexity: O(n)
O(n) to fill all element of aux

Space Complexity: O(n)
Extra space O(n) for aux

Runtime: 46 ms, faster than 28.61% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 97.68% of Python3 online submissions for Climbing Stairs.

"""
class Solution:
    def climbStairs(self, n):
        aux = [1] * (n+1)
        for k in range(2, n+1):
            aux[k] = aux[k-1] + aux[k-2]
        return aux[n]


def test_solution():
        inp = [2,3, 45]
        out = [2,3, 1836311903]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.climbStairs(inp[i])
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()



