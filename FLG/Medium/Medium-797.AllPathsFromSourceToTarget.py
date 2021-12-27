"""
797. All Paths From Source to Target

Main Idea: BFS
create queue
[0]
[0,1]
[0,2]
[0,1,3]
[0,2,3]

Pop paths from queue
If last element == target, add path into result


Time complexity:

Space complexity: extra space for q

Runtime: 92 ms, faster than 95.86% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 15.6 MB, less than 75.49% of Python3 online submissions for All Paths From Source to Target.
"""
class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        q = [[0]]
        target = len(graph) - 1

        while q:
            path = q.pop()
            if path[-1] == target:
                res.append(path)
            else:
                for adj_node in graph[path[-1]]:
                    q.append(path + [adj_node])

        return res


def test_solution():
    inp = [[[1,2],[3],[3],[]],
           [[4, 3, 1], [3, 2, 4], [3], [4], []]
          ]
    out = [[[0,2,3],[0,1,3]],
           [[0, 1, 4], [0, 1, 2, 3, 4], [0, 1, 3, 4], [0, 3, 4], [0, 4]]
          ]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.allPathsSourceTarget(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()