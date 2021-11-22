"""
1281. Subtract the Product and Sum of Digits of an Integer  (Easy)

Time Complexity: O(n)   n - number of digits

Space Complexity: O(n)

Runtime: 39 ms, faster than 19.53% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 14.3 MB, less than 40.92% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]

        sum = 0
        product = 1
        for k in digits:
            sum += k
            product *= k

        return product - sum


def test_solution():
    inp = [234, 4421, 0]
    out = [15, 21, 0]
    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.subtractProductAndSum(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()