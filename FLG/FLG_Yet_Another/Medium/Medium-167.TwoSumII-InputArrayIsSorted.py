"""
167. Two Sum II - Input Array Is Sorted (Medium)

Main Idea.
Two Pointers and Binary Search

1) Start = 0
2) nums[0] == 2, so we want to find 7  (9-2=7)  in subarray nums[1:]
3) If there is not 7,
   increment Start
4) if start is on the last index + 1 :
   Stop iteration


Time complexity: O(NlogN)

Space complexity: O(1)

Runtime: 168 ms, faster than 8.36% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.9 MB, less than 7.25% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

"""
class Solution:
    def twoSum(self, nums, tar):
        def _bin_search(arr, lo, hi, tar):
            if lo > hi: return False
            if tar < arr[lo] or arr[hi] < tar: return False

            while lo <= hi:
                mid = lo + (hi - lo)//2
                if tar == arr[mid]:
                    return mid
                elif tar < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False

        for k in range(len(nums)+1):
            x = tar - nums[k]
            idx =  _bin_search(nums, k+1, len(nums)-1, x)
            if idx is not False:
                return [k+1, idx+1]


def test_solution():
    inp = [ ([2,7,11,15], 9),
            ([2,3,4], 6),
            ([-1,0], -1),
            ]
    out = [[1,2],
           [1,3],
           [1,2]]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.twoSum(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()
