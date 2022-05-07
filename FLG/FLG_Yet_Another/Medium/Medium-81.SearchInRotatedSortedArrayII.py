"""
81. Search in Rotated Sorted Array II (Medium)

Main Idea.
1) Разделить num пополам.
   Если nums[mid] < nums[hi]: то правая половина гарантированно отсортирована
   и пробуем искать target справа бинарным поиском,
2) Если справа не нашли, то задача уменьшилась в два раза
  продолжаем алгоритм сначала, но с левой половиной
3) Если nums[mid] = nums[hi]: то не знаем, какая половина отсортирована
   и запускаем алгоритм рекурсивно и на правой половине и на левой,

Time complexity: O(logN)

Space complexity: O(1)

Runtime: 82 ms, faster than 38.92% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.4 MB, less than 58.55% of Python3 online submissions for Search in Rotated Sorted Array II.

"""
class Solution:
    def search(self, nums, tar) -> bool:
        def _bin_search(arr, lo, hi, x):
            if lo > hi: return False            # Got an empty subarray
            if x < arr[lo] or x > arr[hi]: return False
            mid = (lo + hi) // 2
            if x == arr[mid]:
                return True
            elif x < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
            return _bin_search(arr, lo, hi, x)

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == tar:
                return True
            elif nums[mid] < nums[hi]:     # Half-right is sorted
                res = _bin_search(nums, mid+1, hi, tar)
                if res:
                    return True
                else:
                    hi = mid - 1
            elif nums[mid] > nums[hi]:     # Half-left is sorted
                res = _bin_search(nums, 0, mid-1, tar)
                if res:
                    return True
                else:
                    lo = mid + 1
            elif nums[mid] == nums[hi]:     # don't know which half is sorted
                return self.search(nums[mid + 1:hi], tar) or self.search(nums[lo:mid], tar)

        return False


def test_solution():
    inp = [ ([2,5,6,0,0,1,2], 0),
            ([2,5,6,0,0,1,2], 3),
            ([1], 1),
            ([2], 0),
            ([3,2,2,3], 4),
            ([2, 5, 6, 6, 6, 0, 0, 1, 1, 1, 2, 2], 5),
            ([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2)
          ]
    out = [True, False, True, False, False, True, True]
    # inp = [([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2)]
    # out = [True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.search(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
