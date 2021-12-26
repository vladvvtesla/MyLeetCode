"""
841. Keys and Rooms (Medium)


Main Idea: DFS

Time Complexity:

Space Complexity: extra space for visited

Runtime: 148 ms, faster than 5.19% of Python3 online submissions for Keys and Rooms.
Memory Usage: 15 MB, less than 21.25% of Python3 online submissions for Keys and Rooms.

"""


class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        visited = list()
        graph_stack = list()
        graph_stack.append(0)
        node = 0

        while len(graph_stack) > 0:
            if node not in visited:
                visited.append(node)
            adj_nodes = rooms[node]
            if set(adj_nodes).issubset(set(visited)):
                graph_stack.pop()
                if len(graph_stack) > 0:
                    node = graph_stack[-1]
                    continue
            else:
                remain_els = set(adj_nodes).difference(set(visited))

                first_adj_node = sorted(remain_els)[0]
                graph_stack.append(first_adj_node)
                node = first_adj_node

        return True if len(visited) == len(rooms) else False


def test_solution():
        inp = [[[1],[2],[3],[]],
               [[1, 3], [3, 0, 1], [2], [0]]
               ]
        out = [True, False]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.canVisitAllRooms(inp[i])
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()
