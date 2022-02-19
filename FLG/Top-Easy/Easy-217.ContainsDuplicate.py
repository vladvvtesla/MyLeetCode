"""
217. Contains Duplicate (Top-Easy)

Main Idea.
1) Все встреченные элементы
     если их нет в set(). , то добавить
     если есть, то встретили не уникальный элемент

Time complexity: O(N)

Space complexity: O(N)
Extra space O(N) for set)

Runtime: 599 ms, faster than 46.84% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26.1 MB, less than 30.21% of Python3 online submissions for Contains Duplicate.

"""
class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = set()
        for v in nums:
            if v in s:
                return True
            else:
                s.add(v)
        return False


def test_solution():
    inp = [ [1,2,3,1],
            [1,2,3,4],
            [1,1,1,3,3,4,3,2,4,2]
          ]
    out = [True, False, True]
    # inp = [[1,2,3,1]]
    # out = [True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.containsDuplicate(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
