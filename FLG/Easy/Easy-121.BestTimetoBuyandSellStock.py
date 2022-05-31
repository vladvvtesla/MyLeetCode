"""
121. Best Time to Buy and Sell Stock (Easy)

Main Idea.
Один раз пройтись по массиву.
При необходимости менять локальный минимум
При необходимости менять максимальный профит.
Вернуть получившийся макс_профит

Time Complexity: O(n)
Space complexity: O(1)

Runtime: 1299 ms, faster than 55.57% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 38.15% of Python3 online submissions for Best Time to Buy and Sell Stock.

"""
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 1: return 0     # edge case
        tmpmin_idx = 0
        profit = 0

        for k in range(1,n):
            if prices[k] < prices[tmpmin_idx]:
                tmpmin_idx = k                # 1 - new local min
            profit = max(profit, prices[k] - prices[tmpmin_idx])

        return profit


def test_solution():
    inp = [ [7,1,5,3,6,4],
            [7,6,4,3,1],
          ]
    out = [5, 0]
    # inp = [[7,1,5,3,6,4]]
    # out = [5]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.maxProfit(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
