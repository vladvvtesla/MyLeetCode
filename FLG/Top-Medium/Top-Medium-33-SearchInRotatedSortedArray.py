"""
33. Search in Rotated Sorted Array (Top Medium)

Main Idea:

1. Разделить arr на две части
если arr[mid] > arr[hi],
    то левая половина точно отстортирована,
    и если там нет target, то нужно искать справа

иначе
    правая половина отсортирована
    и если там нет target, то нужно искать слева


Time complexity: O(LogN)

Space complexity: O(N)

Runtime: 55 ms, faster than 36.90% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.5 MB, less than 80.84% of Python3 online submissions for Search in Rotated Sorted Array.
"""
class Solution:
    def search(self, nums, target):

        if len(nums) == 1:
            return 0 if nums[0] == target else -1   # edge Case

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:                # we find target
                return mid

            if nums[mid] > nums[hi]:         # Левая половина отсортирована
                if nums[lo] <= target and target < nums[mid]:  # target нужно искать слева
                    hi = mid - 1
                else:
                    lo = mid + 1                               # target нужно искать справа
            else:                            # правая половина отсортирована
                if nums[mid] < target and target <= nums[hi]:  # target нужно искать срава
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1                                              # если не нашли


def test_solution():
    inp = [
           ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
           ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 0),
           ([2, 3, 4, 5, 6, 7, 8, 9, 0, 1], 0),
           ([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 0),
           ([4, 5, 6, 7, 8, 9, 0, 1, 2, 3], 0),
           ([5, 6, 7, 8, 9, 0, 1, 2, 3, 4], 0),
           ([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], 0),
           ([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], 0),
           ([8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 0),
           ([9, 0, 1, 2, 3, 4, 5, 6, 7, 8], 0),
           ([4, 5, 6, 7, 0, 1, 2], 0),
           ([4, 5, 6, 7, 0, 1, 2], 3),
           ([1], 0),
           ([4, 5, 6, 7, 8, 1, 2], 6),
           ([5, 1, 2, 3, 4], 1),
          ]
    out = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 4, -1, -1, 2, 1,]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.search(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()