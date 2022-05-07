"""
81. Search in Rotated Sorted Array II (Medium)

Main Idea.

Time complexity: O(LogN)

Space complexity: O(1)

Runtime: 64 ms, faster than 69.30% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.5 MB, less than 21.65% of Python3 online submissions for Search in Rotated Sorted Array II.

"""
class Solution:
    def search(self, nums, target) -> bool:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid]==target: return True
            if nums[l]==nums[mid] and nums[mid]==nums[r]:
                l,r=l+1,r-1
            elif nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid + 1
        return False


def test_solution():
    inp = [ ([2,5,6,0,0,1,2], 0),
            ([2,5,6,0,0,1,2], 3),
            ([1], 1),
            ([2], 0),
            ([3,2,2,3], 4),
            ([2, 5, 6, 6, 6, 0, 0, 1, 1, 1, 2, 2], 5),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2)
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
