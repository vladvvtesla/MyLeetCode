"""
1769. Minimum Number of Operations to Move All Balls to Each Box (Medium) Array


Main Idea:

Time Complexity: Brute-Forse O(n^2)

Space Complexity: O(n)
Runtime: 8225 ms, faster than 10.15% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
Memory Usage: 14.2 MB, less than 87.08% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.

"""


class Solution:
    def minOperations(self, boxes: str):
        import itertools

        n = len(boxes)
        a = [0] * n

        for i, k in itertools.product(range(n), range(n)):
            if boxes[k] == "1":
                a[i] += abs(k - i)

        return a


def test_solution():
        inp = ["110", "001011"]
        out = [[1,1,3],[11,8,5,4,3,4]]
        # inp = ["110",]
        # out = [[1,1,3], ]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.minOperations(inp[i])
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()



