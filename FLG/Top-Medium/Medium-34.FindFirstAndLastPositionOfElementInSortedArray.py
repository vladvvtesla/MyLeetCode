"""
34. Medium Find First and Last Position of Element in Sorted Array

Main Idea:
1. Сначала бинарным поиском ищем левую границу
2. Если нашли,
   то ищем правую границу
   и возвращаем [lo,hi]
3.  если не нашли lo, то возвращаем [-1,-1]

После нахождения mid
1. если tar < mid, ищем дальше слева
2. если tar > mid, ищем дальше ссправа
3. если tar = mid,
    если direct = left ищем дальше слева
    если direct = right ищем дальше слева

Time complexity:  log(n)

Space Complexity: log(n)


Runtime: 107 ms, faster than 23.96% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 54.72% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""
class Solution:
    def searchRange(self, nums, target):

        def _binsearch(arr, lo, hi, tar, start):
            if len(arr) == 0: return -1                 # Edge Case
            if tar < arr[lo] or tar > arr[hi]:
                return -1                               # Edge Case

            # Iterative binary search
            while lo < hi:

                # if lo == hi:
                #     return lo if tar == arr[lo] else -1      # Base Case  - Found or Not Found

                if start == 'left':
                    mid = (lo + hi) // 2
                else:
                    mid = ((lo + hi + 1) // 2)               # нужно, чтобы выбирался правый индекс из двух [8,8]

                if arr[mid] > tar:                           #  Продолжаем искать в левом подмассиве без mid
                    hi = mid - 1
                elif arr[mid] < tar:                         #  Продолжаем искать в правом подмассиве без mid
                    lo = mid + 1
                elif arr[mid] == tar and start == 'left':    #  Продолжаем искать в левом подмассиве, включая mid
                    hi = mid
                elif arr[mid] == tar and start == 'right':   #  Продолжаем искать в правом подмассиве, включая mid
                    lo = mid

            if lo == hi:
                return lo if tar == arr[lo] else -1          # Base Case  - Found or Not Found


        lo = _binsearch(nums, 0, len(nums)-1, target, start='left')

        # Если не нашли  lo, то можно не искать hi
        if lo == -1:
            return [-1,-1]
        else:
            # Если нашли lo, то hi следует искать в arr[lo:]
            hi = _binsearch(nums, lo, len(nums)-1, target, start='right')

        return [lo, hi]


def test_solution():
    inp = [([5,7,7,8,8,10],8),
           ([5,7,7,8,8,10],6),
           ([],0),
           ([5,7,7,8,8,10,12],12),
           ([5,7,7,8,8,10,12],16),
           ([8,8,8,8,8,8],8),
           ([2,2],1)]
    # inp = [([5,7,7,8,8,10,12],12)]
    out = [[3,4], [-1,-1], [-1,-1], [6,6],[-1,-1],[0,5],[-1,-1]]
    # out = [[6,6]]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.searchRange(inp[i][0],inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()