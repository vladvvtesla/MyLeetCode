"""
169. Majority Element (Easy but in Top-Medium List may be due tu follow-up)

Main Idea.
1)  Пройтись по всему nums,
 k-указатель поставить на 0-й элемент
 Compare cur and k
 If cur == k : find new answer -> res += 1
 If cur !=k


( Easy Way
count al elements in a dictionary
and return Key for max value
Runtime: 275 ms, faster than 20.27% of Python3 online submissions for Majority Element.
Memory Usage: 15.6 MB, less than 54.66% of Python3 online submissions for Majority Element.)

Follow-UP
Time complexity: O(n)

Space Complexity: O(1)



Space complexity: O (N*M)
"""
class Solution:
    def majorityElement(self, nums):
        aux = {}
        for v in nums:
            if v not in aux.keys():
                aux[v] = 1
            else:
                aux[v] += 1

        top = max(aux.values())
        for k,v in aux.items():
            if v == top:
                return k




def test_solution():
    inp = [ [3,2,3],
            [2,2,1,1,1,2,2],
            [2],
            [2,2,1,1,1],
            [1,1,1,2,2],
            [1, 2, 1, 1, 2],
            [1,2,3,1,2,3,3,3,2]
          ]
    out = [3, 2, 2, 1, 1, 1, 3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.majorityElement(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_solution()
