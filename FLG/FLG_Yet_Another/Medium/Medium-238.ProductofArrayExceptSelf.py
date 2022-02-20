"""
238. Product of Array Except Self (Medium)

Main Idea.
1) Создать вспомогательный массив умножая все слева направо l_arr
2) Создать вспомогательный массив умножая все справа налево r_arr
3) Создать res, умножая res[k] = l_arr[k-1] * r_arr[k+1]
При этом расширить l_arr и r_arr и добавить справа и слева 1
nums =        [1,2,3,4]
l_arr = [1] + [1, 2,  6,24] + [1]
r_arr = [1] + [24,24,12, 4] + [1]
res =         [24,12,8,6]


Time complexity: O(n)
Создать l_arr: O(n+2)
Создать r_arr: O(n+2)
Создать res: O(n)
Итого: 3*O(n) = O(n)

Space complexity: O(n)
Создать l_arr: O(n+2)
Создать r_arr: O(n+2)
Создать res: O(n)
Итого: 3*O(n) = O(n)

Runtime: 277 ms, faster than 61.28% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.4 MB, less than 24.11% of Python3 online submissions for Product of Array Except Self.

"""
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        l_arr = [1] * (n + 2)
        for k, v in enumerate(nums):
            l_arr[k+1] = l_arr[k] * v

        r_arr = [1] * (n + 2)
        for k in range(len(r_arr)-2,0,-1):
            r_arr[k] = r_arr[k+1] * nums[k-1]

        res = [l_arr[k-1] * r_arr[k+1] for k in range(1,n+1)]

        return res


def test_solution():
    inp = [ [1,2,3,4],
            [-1,1,0,-3,3],
            [0,0],
            [1,1]
          ]
    out = [[24,12,8,6],
          [0,0,9,0,0],
          [0,0],
          [1,1]]
    # inp = [[1,2,3,4]]
    # out = [[24,12,8,6]]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.productExceptSelf(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
