"""
75. Sort Colors (Top Medium)

Main Idea:
3 pointers
Нужно получить список вида [0,0,1,1,2,2], поэтому

1) бежим по списку пока не достигли конечного индекса (который будет двигаться навстречу)

2) пропускаем начальне 0 и двигаем start
3) пропускаем конечные 2 и двигаем end
4) встреченные cur 0 и 2 перемещаем соответсвенно в начало или конец
5) если подряд идут 1 то двигаем cur

Особый случай, если список начинается с 1 и затем есть 0.

Time complexity: O(n)

Space complexity: O(n)

Runtime: 32 ms, faster than 77.20% of Python3 online submissions for Sort Colors.
Memory Usage: 14.2 MB, less than 75.48% of Python3 online submissions for Sort Colors.

"""
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        cur = 0                    # Cur нужен, когда много 1 в начале или в конце и только потом 0
        while cur <= end:
            print('current nums', nums[start: end+1] )
            print('start', start)
            print('cur', cur)
            print('end', end)

            if nums[start] == 0:   # Проскочили все начальные 0
                start += 1
                cur += 1
                continue
            if nums[end] == 2:     # Проскочили все конечные 2
                end -= 1
                continue

            if nums[start] == 2:   # 2 в конец и все заново
                nums[start], nums[end] = nums[end], nums[start]
                continue

            if nums[end] == 0:    # 0 в начало и все заново
                nums[start], nums[end] = nums[end], nums[start]
                continue

            if nums[cur] == 2:     # 2 в конец и все заново
                nums[cur], nums[end] = nums[end], nums[cur]
                continue

            if nums[cur] == 0:     # 0 в начало и все заново
                nums[cur], nums[start] = nums[start], nums[cur]
                continue

            cur += 1


def test_solution():
    inp = [[2,0,2,1,1,0],
            [2,0,1],
            [1,1,1,0],
            [1,1,1],
            [2,2,2],
            [0],
            [1],
            [1,2,0],
            [1,2],
            [0,1],
            [0,2],
            [2,1,2],
            [1,0,1]
           ]
    out = [[0,0,1,1,2,2], [0,1,2], [0,1,1,1], [1,1,1], [2,2,2], [0], [1],
           [0,1,2], [1,2], [0,1], [0,2], [1,2,2], [0,1,1]]
    sol = Solution()

    for i in range(len(inp)):
        print('inp[i] before', inp[i])
        sol.sortColors(inp[i])
        print('inp[i] after', inp[i])
        print("Test", i + 1, ":", "OK\n" if inp[i] == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()