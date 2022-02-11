"""

283. Easy - Move Zeroes

Изначально считаем, что нужно меняться с индексом 0
Делаем для всех элементов arr:
Если встертили 0,
    то ничего не делаем, то есть
    с кем меняться остается по прежнему с индексом 0
если встретили не 0,
    то  1) перемена местами arr[metka] и arr[curr]
        2) увеличиваем с кем меняться на 1

таким образом после всех перестановок местами, у нас все 0 окажутся в конце массива,
Do not return anything, modify nums in-place instead.

Time Complexity:   O(n)
Space Complexity:  O(n)

Runtime: 48 ms, faster than 75.03% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 64.69% of Python3 online submissions for Move Zeroes.
"""

class Solution:
    def moveZeroes(self, nums):
        x_idx = 0          # С кем меняться
        for k,j in enumerate(nums):                             # O(n)
            if j != 0:                                          # O(1)
                nums[k], nums[x_idx] = nums[x_idx],nums[k]      # O(1)
                x_idx += 1                                      # O(1)

        return nums    # Для leetcode это не нужно, только для теста

def test_moveZeroes():
    nums = [0, 1, 0, 3, 12]

    sol = Solution()
    test_res = sol.moveZeroes(nums)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == [1,3,12,0,0] else "Failed\n")


if __name__ == '__main__':
    test_moveZeroes()