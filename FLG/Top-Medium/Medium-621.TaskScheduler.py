"""
621. Task Scheduler (Medium)

Main Idea.
https://www.youtube.com/watch?v=CHlCkJadQ7o

Time complexity: O(N)

Space complexity: O(N)
O(N) for aux dictionary

Runtime: 753 ms, faster than 34.58% of Python3 online submissions for Task Scheduler.
Memory Usage: 14.4 MB, less than 83.65% of Python3 online submissions for Task Scheduler.

"""
class Solution:
    def leastInterval(self, tasks, n) -> int:
        aux_d = {}
        for t in tasks:
            if t in aux_d.keys():
                aux_d[t] += 1
            else:
                aux_d[t] = 1

        lst = sorted(aux_d.values(), reverse=True)
        max_number = lst[0]

        k = 0
        counter = 0
        while k < len(lst) and lst[k] == max_number:
            counter += 1
            k += 1

        ret = (max_number - 1) * (n + 1) + counter
        return max(ret, len(tasks))


def test_solution():
    inp = [ (["A","A","A","B","B","B"], 2),
            (["A","A","A","B","B","B"], 0),
            (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
          ]
    out = [8,6,16]
    # inp = [(["A","A","A","B","B","B"], 2)]
    # out = [8]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.leastInterval(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
