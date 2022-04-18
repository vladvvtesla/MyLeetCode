"""
Easy - 933 Number of Recent Calls


Main Idea:

Time complexity:

Space Complexity:

Runtime: 6214 ms, faster than 5.02% of Python3 online submissions for Number of Recent Calls.
Memory Usage: 19.7 MB, less than 17.78% of Python3 online submissions for Number of Recent Calls.

"""


class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t):
        count = 0
        self.calls.append(t)
        for k in range(len(self.calls)-1, -1, -1):
            if self.calls[-1] - self.calls[k] <= 3000:
                count += 1
            else:
                break
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

def test_solution():
    inp = [[1,100,3001,3002],
          ]
    out = [[1,2,3,3],
            ]

    for i in range(len(inp)):
        sol = RecentCounter()
        test_res = []
        for k in range(len(inp[i])):
            param = sol.ping(inp[i][k])
            test_res.append(param)

        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()